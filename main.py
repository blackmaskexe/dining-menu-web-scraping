from bs4 import BeautifulSoup
import requests
import certifi
import html5lib

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

# parsing the raw html into beautiful soup object format:
soup = BeautifulSoup(raw_site_html, 'html5lib')

# storing parsed tables that contain menu information:
all_tables = soup.find_all('table')

# storing all the titles for the tables:
table_titles = [h2.get_text(strip=True) for h2 in soup.find_all('h2', class_="block__heading heading_primary")]

# creating an empty array that will house all the menu data after the loop:
menu_data = []

for i in range(len(all_tables)):
    table = all_tables[i] # Accessing the table using its index
    # getting all the horizontal headers names for the table:
    col_headers = [header.get_text(strip=True) for header in table.find_all('th', scope='col')]

    table_data = {
        "table_title": table_titles[i],
    }

