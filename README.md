# Mission to Mars Web-scraping Challenge
# Overview
### This project utilizes web-scraping, noSQL, and app tools to create a webpage that displays the latest information about the Mars mission.
# Tools used
### Splinter reads in dynamically-rendered html from four websites and automates the clicking of buttons to navigate websites during scraping.
### Beautiful Soup extracts content from each html file.
### Pandas is used to read in tabular content from one of the websites and clean it.
### Content is stored in a Mongo database, accessed with Pymongo. 
### A Flask app is used to present the data on a webpage styled with a Flask template.
# Files
### app.py is a Flask app that contains two routes that can be used independently to 1) Display The current contents of a Mongo database and 2) To scrape new data as needed.The scraping functionality can take several minutes to complete and is therefore separated from the root route to ensure that at least an initial home page loads quickly. The root route displays the current contents of a Mongo database using a Flask template (index.html) for styling. The scrape route activates a script (scrape_mars.py) that scrapes the latest Mars mission images and facts from various websites and returns a dictionary full of content. app.py uses Pymongo to connec to a Mongo database and save the new content.

### scrape_mars.py is a python script that uses Splinter and Beautiful soup to scrape four different websites and compile the scraped content into a single dictionary which is passed to app.py.
### index.html is a Flask HTML template that works with a Flask app called app.py. It receives a dictionary called latest_content from the Flask app, extracts content from the dictionary, and displays it. A Bootstrap grid is used for placement and a Bootstrap button navigates to the /scrape route in app.py to scrape new content.