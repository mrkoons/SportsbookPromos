from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
from tkinter import *
import os

folder = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(folder, 'DraftKings.py')
print(file)

url = "https://sportsbook.draftkings.com/featured"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


title = soup.find_all("div", class_="promo-offer-card__title")
description = soup.find_all("div", class_="promo-offer-card__description")
promo = np.dstack((title, description))

# print(promo)

# How do I get the popup from crontab schedule, need to cd to folder
# How to run python from terminal with external modules
# Read emails from terminal
# Need to switch to python 3?
# mail, t

root = Tk()

myLabel = Label(root, text=promo)

myLabel.pack()

root.mainloop()