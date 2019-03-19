# --------------------------------------------------- #
#
# Events Scraper: gets the upcoming events from
# The Hill Happenings, then updates csv file with
# latest food events as an array of dictionaries.
# Bri's Version
#
# --------------------------------------------------- #

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://www.hillhappenings.com/"
my_url = base_url + "?category=Food"

# while in the events sections, grab:
# Title
# Description of the event
# links of events
# Datetime(s) of event
# Image url of the event
# Reservation link

# opening up connection, grabbing the page
uClient = uReq(my_url)
#offloads connection content into a variable
page_html = uClient.read()
# closes connection
uClient.close()

# html parsing
soup = BeautifulSoup(page_html, "html.parser")

# get the main table results
results = soup.findAll("div", attrs={"class":"eventlist-column-info"})

#record event info
events = []

# Create loop to grab event info
for info in results:

    #stores each events's info
    event = {}

    #grab date
    date = info.find("time", {"class":"event-date"})
    date_text = date.text.strip()
    event["date"] = date_text

    #grab start and end times
    time_start = info.find("time", {"class":"event-time-12hr-start"})
    time_start_text = time_start.text.strip()

    time_end = info.find("time", {"class":"event-time-12hr-end"})
    time_end_text = time_end.text.strip()

    startend_time = time_start_text + "," + time_end_text
    event["start and end times"] = startend_time

    #grab title
    title = info.find("h1", {"class": "eventlist-title"})
    title_text = title.a.text.strip()
    event["title"] = title_text

    #grab description
#    description = info.find("div", {"class": "eventlist-excerpt"})
    description = info.find("p", attrs={"style":"white-space:pre-wrap;"})
    description_text = description #somehow get the text in here
    event["description"] = description_text

    #grab links
    link = info.find("h1", {"class": "eventlist-title"})
    link_text = link.a["href"]
    website_text = (base_url + link_text)
    event["website"] = website_text

    #grab location
#    location = info.find("li", {"class":"eventlist-meta-item eventlist-meta-address event-meta-item"})
#    location_text = location.text.strip()
#    event["location"] = location_text

## location is given in the map

    #location map link
    map_link = info.find("li", {"class":"eventlist-meta-item eventlist-meta-address event-meta-item"})
    map_link_text = map_link.a["href"]
    event["map and location"] = map_link_text

    #appends all events
    events.append(event)


Headlines = ["date", "start and end times", "title", "description", "website", "map and location"]

try:
    # Open the csv to import data
    with open("food_on_the_hill.csv", "w", newline='', encoding="utf8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=Headlines)
        writer.writeheader()
        for event in events:
            writer.writerow(event)
except IOError:
    print("I/O Error")


