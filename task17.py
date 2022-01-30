"""Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage."""

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.nytimes.com/"
web_text = requests.get(url)
web_text_html = web_text.text

soup = BeautifulSoup(web_text_html)
soup.find_all(class_="css-kaamp8") # class="css-eylb5n" -> it's a place where titles are

for article_heading in soup.find_all(class_="css-kaamp8"):
    print(article_heading)





