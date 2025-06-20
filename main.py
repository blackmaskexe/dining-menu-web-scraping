import os

from bs4 import BeautifulSoup
import requests
import certifi
import html5lib
from google import genai
from dotenv import load_dotenv

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
        "Main Course": [
          "Croissant",
          "English Muffins",
          "Canadian Bacon",
          "Sausage or Turkey Patty",
          "American Cheese",
          "Eggs",
          "Triangle Potato"
        ],
        "Greens Station": [
          "Oatmeal & Toppings",
          "Breakfast Salad Bar"
        ],
        "Your Call Station": [
          "Eggs & Omelet Bar"
        ],
        "Bakery Station": [
          "Apple Cinnamon Muffins",
          "Assorted Danish Pastries"
        ],
        "Other Open Stations": [
          "Waffle & Toppings"
        ]
      },
      "Tuesday": {
        "Main Course": [],
        "Greens Station": [],
        "Your Call Station": [],
        "Bakery Station": [],
        "Other Open Stations": []
      }
    }
  },
  {
    "table_title": "Lunch",
    "menu_on_days": {
      "Monday": {
        "Main Course": [],
        "Your Call": [],
        "World Eats": [],
        "Bakery": [],
        "Other Open Stations": []
      }
    }
  },
  {
    "table_title": "Dinner",
    "menu_on_days": {}
  },
  {
    "table_title": "Saturday Brunch",
    "menu_on_days": {
      "Saturday": {
        "Main Course": [
          "Scrambled Eggs w/Cheese",
          "Texas French Toast",
          "Hashbrowns",
          "Sausage Link"
        ],
        "World Eats Station": [],
        "Greens Station": [],
        "Bakery": [],
        "Other Open Stations": []
      }
    }
  }
]
# literally pasting this menu to an ai, and giving instructions on how it should format it:
ai_instructions = (f"I will paste the raw html content of a website, and you will format it as a JSON array containing "
                   f"json objects and constructs. This is the html code for a website that contains the menu at "
                   f"campus locations at a University. Your response should look like the following based on the "
                   f"content: {str(sample_response)}. Your response should only contain the JSON object, and nothing "
                   f"else. If something goes wrong, just return an empty JSON array, but you do have to always return "
                   f"valid json response.")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=ai_instructions + relevant_content_string,
)

print(response.text)
