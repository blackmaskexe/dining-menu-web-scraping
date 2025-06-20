## Purpose of the script:
- Web scrape the contents of the menu at dining locations at St. Thomas
- Be able to handle dynamic table content, and store data gracefully (into a format that can be easily converted to JSON)

## Notes while using this scaping tool:
- This scraper is sensitive to changes to the dining menu website:
    - html tag and attribute changes might break the functionality of the scraper
    - potential fixes to this could be using an AI call to parse the content of the page at once (running it even once a day would cost next to nothing!)

## Expected format for the output:
```json
[
  {
    "table_title": "Breakfast",
    "menu_on_days":  {
      "Monday": {
        "Main Course": ["Croissant", "English Muffins", "Canadian Bacon", "Sausage or Turkey Patty", "American Cheese", "Eggs", "Triangle Potato"],
        "Greens Station": ["Oatmeal & Toppings", "Breakfast Salad Bar"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Apple Cinnamon Muffins", "Assorted Danish Pastries"],
        "Other Open Stations": ["Waffles & Toppings"]
      },
      "Tuesday": {
        "Main Course": ["Croissant", "English Muffins", "Canadian Bacon", "Sausage or Turkey Patty", "American Cheese", "Eggs", "Triangle Potato"],
        "Greens Station": ["Oatmeal & Toppings", "Breakfast Salad Bar", "Cantaloupe"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Chocolate Chip Muffins", "Mini Cinnamon Rolls"],
        "Other Open Stations": ["Waffles & Toppings"]
      },
      "Wednesday": {
        "Main Course": ["Croissant", "English Muffins", "Canadian Bacon", "Sausage or Turkey Patty", "American Cheese", "Eggs", "Triangle Potato"],
        "Greens Station": ["Oatmeal & Toppings", "Breakfast Salad Bar", "Lunch Bunch Grapes"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Orange Blossom Muffins", "Apple Turnover"],
        "Other Open Stations": ["Waffles & Toppings", "Bagels & Toppings"]
      },
      "Thursday": {
        "Main Course": ["Croissant", "English Muffins", "Canadian Bacon", "Sausage or Turkey Patty", "American Cheese", "Eggs", "Triangle Potato"],
        "Greens Station": ["Oatmeal & Toppings", "Breakfast Salad Bar", "Kiwi"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Cappuccino Muffins", "Glazed Cake Donuts"],
        "Other Open Stations": ["Waffles & Toppings"]
      },
      "Friday": {
        "Main Course": ["Croissant", "English Muffins", "Canadian Bacon", "Sausage or Turkey Patty", "American Cheese", "Eggs", "Triangle Potato"],
        "Greens Station": ["Oatmeal & Toppings", "Breakfast Salad Bar", "Pineapple"],
        "Your Call Station": ["Eggs & Omelet Bar"],
        "Bakery Station": ["Blueberry Muffins", "Mini Caramel Rolls"],
        "Other Open Stations": ["Waffles & Toppings"]
      }
    }
  }
]
```

## How to run:
1. Clone the project
```bash
git clone https://github.com/blackmaskexe/dining-menu-web-scraping.git
cd dining-menu-web-scraping
```
2. PIP Install all the requirements:
```bash
pip install -r requirements.txt
```
- note that you might need to replace pip with pip3 if the above does not work

3. Create an API key for Gemini AI
3. Create a .env file in your project folder
4. create a secret named GEMINI_API_KEY in your .env file like this:
```.env
GEMINI_API_KEY=YOURAPIKEYWITHOUTQUOTES123456
```
5. Run main.py
```python
python main.py
```