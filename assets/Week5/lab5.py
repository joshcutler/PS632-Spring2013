# Scraper to collect petition info from petitions.whitehouse.gov

import csv 
import re 
import time
import urllib
import urllib2 
from BeautifulSoup import BeautifulSoup

# What page? 
page_to_scrape = 'https://petitions.whitehouse.gov/petitions'

# What info do we want? 
headers = ["Summary", "Signatures"]

# Where do we save info?
filename = "whitehouse-petitions.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)
