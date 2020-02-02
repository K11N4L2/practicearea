
import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib3
import lxml
import html5lib

# webbrowser.open('https://www.bbc.co.uk/news')
page = requests.get("https://www.bbc.co.uk/news")

soup = BeautifulSoup(page.content, 'html.parser')

headlines = soup.find_all('div', class_='gs-c-promo-heading')
# headline = soup.select('promo-heading')
# headlines = soup.prettify(headlines)

headline = soup.title.string('div', class_='gs-c-promo-heading')

print(headline)
print(headlines)

# fix not working - find tags/classes / id / string / findall() 
# panda's? 
