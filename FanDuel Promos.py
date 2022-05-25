from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np

url = "https://sportsbook.fanduel.com/sports"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

title = soup.find_all("meta")
# description = soup.find_all("div", class_="promo-offer-card__description")

print(title)
# print(soup)