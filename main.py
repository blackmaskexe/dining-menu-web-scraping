import os

from bs4 import BeautifulSoup
import requests
import certifi
import html5lib
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()


# this array contains list of dining locations, and their associated menu website links to webscrape
dining_location_menus = [{
    "index": 0,
    "location": "The View",
    "dining_menu_link": "https://www.stthomas.edu/dining/locations-menus-hours/the-view/menu/index.html"
}, {
    "index": 1,
    "location": "Northsider",
    "dining_menu_link": "https://www.stthomas.edu/dining/locations-menus-hours/northsider/menu/index.html"
}]

selected_dining_location_index = 0
selected_dining_location = dining_location_menus[selected_dining_location_index]

# requesting the contents of the dining menu website:
request = requests.get(selected_dining_location['dining_menu_link'], verify=False)
raw_site_html = request.text

soup = BeautifulSoup(raw_site_html, 'html5lib')
relevant_content = soup.find('div', id='content')
relevant_content_string = str(relevant_content)


# creating a sample format in which the AI has to return a response.
sample_response = [
  {
    "table_title": "Breakfast",
    "menu_on_days": {
      "Monday": {
        "Main Course": ["Croissant"],
        "Greens Station": ["Oatmeal & Toppings"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Apple Cinnamon Muffins"],
        "Other Open Stations": ["Waffle & Toppings"]
      },
      "Tuesday": {
        "Main Course": ["Croissant"],
        "Greens Station": ["Cantaloupe"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Chocolate Chip Muffins"],
        "Other Open Stations": ["Waffles & Toppings"]
      },
      "Wednesday": {
        "Main Course": ["Croissant"],
        "Greens Station": ["Lunch Bunch Grapes"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Orange Blossom Muffins"],
        "Other Open Stations": ["Waffles & Toppings"]
      },
      "Thursday": {
        "Main Course": ["Croissant"],
        "Greens Station": ["Kiwi"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Cappuccino Muffins"],
        "Other Open Stations": ["Waffles & Toppings"]
      },
      "Friday": {
        "Main Course": ["Croissant"],
        "Greens Station": ["Pineapple"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Blueberry Muffins"],
        "Other Open Stations": ["Waffles & Toppings"]
      }
    }
  },
  {
    "table_title": "Lunch",
    "menu_on_days": {
      "Monday": {
        "Main Course": ["Beef Chili Dog"],
        "Your Call": ["Pad Thai Stir Fry Bar"],
        "World Eats": ["Fish Tacos"],
        "Bakery": ["Chocolate Chocolate Chip Cookies"],
        "Other Open Stations": ["Deli"]
      },
      "Tuesday": {
        "Main Course": ["Open-faced Turkey Sandwich"],
        "Your Call": ["Pad Thai Stir Fry Bar"],
        "World Eats": ["Piada Bar"],
        "Bakery": ["Oatmeal Butterscotch Cookies"],
        "Other Open Stations": ["Grill"]
      },
      "Wednesday": {
        "Main Course": ["Philly Steak Sandwich"],
        "Your Call": ["Pad Thai Stir Fry Bar"],
        "World Eats": ["Honey Chili Lime Shrimp Tacos"],
        "Bakery": ["Peanut Butter Cookies"],
        "Other Open Stations": ["Pasta Bar"]
      },
      "Thursday": {
        "Main Course": ["Grilled Mediterranean Chicken Breast"],
        "Your Call": ["Pad Thai Stir Fry Bar"],
        "World Eats": ["Nacho Bar"],
        "Bakery": ["Sugar Cookies"],
        "Other Open Stations": ["Pizza Bar"]
      },
      "Friday": {
        "Main Course": ["Supreme Grilled Cheese"],
        "Your Call": ["Pad Thai Stir Fry Bar"],
        "World Eats": ["Chipotle Citrus BBQ Chicken"],
        "Bakery": ["Chocolate Peanut Butter M&M Cookies"],
        "Other Open Stations": ["Soups"]
      }
    }
  },
  {
    "table_title": "Dinner",
    "menu_on_days": {
        "Monday": {
            "Main Course": ["Grilled Balsamic Chicken & Pomodoro Relish"],
            "Your Call Station": ["Pad Thai Stir Fry Bar"],
            "World Eats Station": ["Beef Chow Mein"],
            "Bakery": ["Chocolate Chocolate Chip Cookies"],
            "Other Open Stations": ["Deli"]
        },
        "Tuesday": {},
        "Wednesday": {},
        "Thursday": {},
        "Friday": {},
        "Saturday": {}
    }
  },
  {
    "table_title": "Saturday Brunch",
    "menu_on_days": {
      "Saturday": {
        "Main Course": ["Scrambled Eggs w/Cheese"],
        "World Eats Station": ["Cheese Manicotti"],
        "Greens Station": ["Oatmeal & Toppings"],
        "Bakery": ["Banana Nut Muffins"],
        "Other Open Stations": ["Deli"]
      }
    }
  }
]
# literally pasting this menu to an ai, and giving instructions on how it should format it:
ai_instructions = (f"I will paste the raw html content of a website, and you will format it as a JSON array containing "
                   f"json objects and constructs. This is the html code for a website that contains the menu at "
                   f"campus locations at a University. Your response should look like the following based on the "
                   f"content: {str(sample_response)}. (Please note that this is just a skeleton response. Your "
                   f"response should contain all the information in the website, and not miss any entry for any item "
                   f"or day. Your response should only contain the JSON object, and nothing"
                   f"else. If something goes wrong, just return an empty JSON array, but you do have to always return "
                   f"valid json response.")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=ai_instructions + relevant_content_string,
)

cleaned_response = response.text.strip().strip("```").lstrip("json").strip()

menu_data = json.loads(cleaned_response)
print(menu_data)