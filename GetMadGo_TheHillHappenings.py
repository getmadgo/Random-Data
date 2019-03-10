from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
import csv
import csv
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import schedule
from urllib.request import urlopen
import re


##Project Scrape Get Mad Go, Food events on the Hill##

ssl._create_default_https_context = ssl._create_unverified_context

my_url = "https://www.hillhappenings.com/?category=Food"

# opening up connection, grabbing the page

uClient = uReq(my_url)

# offloads connection content into a variable

page_html = uClient.read()

# closes connection

uClient.close()

# html parsing

page_soup = soup(page_html, "html.parser")

#Writet the pattern of data found in page source
#pattern =

# grabs each product

dates = page_soup.findAll("li", attrs={"class":"eventlist-meta-item eventlist-meta-date event-meta-item"})
titles = page_soup.findAll("h1", attrs={"class":"eventlist-title"})

#Holds main data
data = []

#Holds dates
d = []

#Create a function that returns date
def Getdates(str):

    for i in dates:
        for num in i.findAll("time", {"class": "event-date"}):
            listed_dates = (num["datetime"])
            d.append(listed_dates)

    return d

#Holds titles
t =[]

#Create a function that returns titles
def Gettitles(str):

    for tit in page_soup.findAll("a", {"class": "eventlist-title-link"}):
        listed_titles = tit.string
        t.append(listed_titles)

    return t


# Add data to one large data set

datesList = Getdates(d)
titlesList = Gettitles(t)

instance = [datesList, titlesList]
data.append(instance)


#add dates to data
#data.append([listed_titles, listed_dates])


# Import data into csv
with open("food_on_the_hill.csv", "a") as csv_file:
    writer = csv.writer(csv_file)

    # Loop through every listed date
    for food in data:
        writer.writerow(food)

