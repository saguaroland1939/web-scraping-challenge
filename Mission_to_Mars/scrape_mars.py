# This Python script scrapes Mars-related news from four different websites and delivers the content to a Flask app for presentation.

# Import dependencies
from splinter import Browser # For scraping JavaScript-rendered pages and clicking buttons.
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager # Required by Splinter.
import pandas as pd
import pymongo

# Set up Splinter:
# Install Chrome driver manager (if not already present) and store path for use by Splinter.
chrome_driver_path = {'executable_path': ChromeDriverManager().install()}
# Instantiate Splinter Browser object.
browser = Browser('chrome', **chrome_driver_path)


# This function scrapes the latest Mars news and images from four different websites, stores the scraped content in a Mongo database, 
# and returns a Python dictionary.
#def scrape():
    # Convert scraping code from Jupyter Notebook into this function. 


    # store scraped content in a Mongo db, overwriting the existing document each time the function is called.


    # return a single Python dictionary.