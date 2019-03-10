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

my_url = "https://www.hillhappenings.com/"

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

titles = page_soup.findAll("h1", {"class":"eventlist-title"})
descriptions = page_soup.findAll("p", {"class":"hidden-xs"})
image_divs = page_soup.findAll("div", {"class":"col-sm-4 col-xs-4"})

for events in page_soup.findAll("div", {"class":"media row col-lg-12 col-md-12 col-sm-12 col-xs-12"}):
    print (events.text)