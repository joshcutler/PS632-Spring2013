# Scraper to collect election 2012 ads from moat.com

import urllib2 
import urllib
import re 
import time
from BeautifulSoup import BeautifulSoup

pages_to_scrape = ['http://www.moat.com/search/results?q=romney',
	'http://www.moat.com/search/results?q=obama']

for i in range(0,2):
	current_page = pages_to_scrape[i]

	if i == 0:
		candidate = 'romney'
	else:
		candidate = 'obama'

	# Open the webpage
	time.sleep(1)
	webpage = urllib2.urlopen(current_page)

	#Parse it
	soup = BeautifulSoup(webpage.read())
	soup.prettify()
        
  # Extract image tags
	images = soup.findAll("img")

	imgurls = []

  # Process image source urls
	for j in range(2, len(images)-3):
	#for j in range(2, 10):

		image = str(images[j])
		# print image

		#try:
		url = re.search('src=".*?"', image).group(0)
		url = url.lstrip('src="')
		url = url.rstrip('"')

		savename = candidate + str(j-1) + '.' + url[-3:]
		urllib.urlretrieve(url, savename)

		print j
		#except: 
		#	pass
