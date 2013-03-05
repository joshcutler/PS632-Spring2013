Today we're working with Application Programming Interfaces (API's).

# Huffington Post

As a first example, we're going to use the Huffington Post [Pollster API](http://elections.huffingtonpost.com/pollster/api). Conveniently for our purposes, there is a Python [library](http://pypi.python.org/pypi/Pollster) that makes working with the API simple. Other journalism publishers also offer API's including [USA Today](http://developer.usatoday.com/docs/read/articles) and [The New York Times](http://developer.nytimes.com/docs). You can find a whole list of politics-related API's [here](http://www.programmableweb.com/apitag/politics). 

First, everyone needs to install the Python library:
`pip install pollster` Then, go through examples in lab4.py. 

# Google 

For the second example, we'll use the Google Maps API. Have everyone go to the [Google developer page](http://developers.google.com) and get an API key. 

Then, work through the code in gmaps.py to illustrate getting lat/long from an address, address from a lat/long, local search, and directions. Have students combine these to iterate through a list of embassy lat/longs and answer a few questions. 