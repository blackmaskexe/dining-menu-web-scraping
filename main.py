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

all_tables = soup.find_all('table')

for table in all_tables:
    # getting all the horizontal headers names for the table:
    col_headers = [header.get_text(strip=True) for header in table.find_all('th', scope='col')]
    print(col_headers, "fein fein fein fein fein fein")
