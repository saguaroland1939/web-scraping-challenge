# This Python script scrapes Mars-related news from four different websites and delivers the content to a Flask app for presentation.
# Splinter is used to scrape html loaded dynamically and automate button clicks. ChromeDriverManager is required to run Splinter.
# Beautiful Soup is used to parse content from html. Pandas is used to scrape the table.

# Import dependencies
from splinter import Browser # For scraping JavaScript-rendered pages and clicking buttons.
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager # Required by Splinter.
import pandas as pd

# This function scrapes the latest Mars news and images from four different websites, stores the scraped content in a Mongo database, 
# and returns a Python dictionary.
def scrape():

    # Create a blank dictionary to return all scraped results.
    dictionary = {}

    # Set up Splinter:
    # Install Chrome driver manager (if not already present) and store path for use by Splinter.
    chrome_driver_path = {'executable_path': ChromeDriverManager().install()}
    # Instantiate Splinter Browser object.
    browser = Browser('chrome', **chrome_driver_path)


    # Collect latest news from mars.nasa.gov:

    # Use Splinter to open webpage in Chrome browser.
    browser.visit("https://mars.nasa.gov/news/")
    # Store html from browser.
    html = browser.html
    # Store html as Beautiful Soup object.
    soup = bs(html, "html.parser")
    # Scrape title of first news article.
    first_article_title = soup.find("div", class_="list_text").a.text
    # Scrape teaser from first news article.
    first_article_teaser = soup.find(class_ = "article_teaser_body").text

    # Insert scraped contents into dictionary. If key already exists, this will overwrite with new value.
    dictionary.update({"news_title": first_article_title, "news_teaser": first_article_teaser})

    # Collect current featured Mars image from jpl.nasa.gov:

    # Store url as string variable.
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Use Splinter to open webpage in Chrome browser.
    browser.visit(url)
    # Use Splinter to click button to open full image.
    browser.links.find_by_partial_text('IMAGE').click()
    # Store html from browser.
    html = browser.html
    # Store html as Beautiful Soup object.
    soup = bs(html, "html.parser")
    # Use Beautiful Soup to search for url of image in the 'carousel' at top of page.
    partial_url = soup.find("article", class_="carousel_item").a["data-fancybox-href"]
    # Concatenate partial url with homepage url.
    mars_image_url = "https://www.jpl.nasa.gov" + partial_url

    # Insert scraped contents into dictionary. If key already exists, this will overwrite with new value.
    dictionary.update({"mars_image_url": mars_image_url})


    # Collect table of Mars facts from space-facts.com:

    # Use Pandas to collect the table and store it in a DataFrame.
    facts_df = pd.read_html("https://space-facts.com/mars/")[0]
    # Convert the DataFrame back to html for subsequent display.
    facts_html = facts_df.to_html(header=None, index = False)

    # Insert scraped contents into dictionary. If key already exists, this will overwrite with new value.
    dictionary.update({"facts_table_html": facts_html})


    # Collect Mars hemisphere images from astrogeology.usgs.gov:

    # Create empty list to hold list of dictionaries.
    hemisphere_images = []
    # Loop through elements 1, 3, 5, and 7 (0, 2, 4, and 6 are blanks).
    for x in range(1, 9, 2):
        # Navigate to product page and load html.
        browser = Browser('chrome', **chrome_driver_path)
        browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
        html = browser.html
        soup = bs(html, "html.parser")
        # Use Splinter to find all links with 'enhanced' in the url
        links = browser.links.find_by_partial_href('enhanced')
        # Use Splinter to click the link.
        links[x].click()
        # Store the html and convert to Beautiful Soup.
        html = browser.html
        soup = bs(html, "html.parser")
        # Use Beautiful Soup to extract hemisphere name.
        title = soup.find(class_="title").text
        # Use Beautiful Soup to extract partial url of image.
        partial_url = soup.find(class_="wide-image")["src"].strip()
        # Append partial_url to home page url to compose full url.
        img_url = "https://astrogeology.usgs.gov" + partial_url
        # Store hemisphere name and image url as dictionary in hemisphere_images.
        hemisphere_images.append({"title": title, "img_url": img_url})
        # Close browser.
        browser.quit()

    # Insert scraped contents into dictionary. If key already exists, this will overwrite with new value.
    dictionary.update({"hemisphere_image_list": hemisphere_images})

    # Returns a single dictionary with all scraped content store as dictionary or list to app.py.
    return dictionary
