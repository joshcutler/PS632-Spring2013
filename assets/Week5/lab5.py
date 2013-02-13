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

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Extract petitions on page
#petitions = soup.findAll("a", href=re.compile('^/petition'))
petitions = soup.findAll("div", attrs={'class':'title'})
print len(petitions)
for petition in petitions:
	print petition 

signatures = soup.findAll("div", attrs={'class':'num-sig'})
print len(signatures)
for signature in signatures:
	print signature



