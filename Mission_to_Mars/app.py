# This Flask app contains two routes that can be used independently to 1) Display The current contents of a Mongo database and 2) To scrape new data as needed.
# The scraping functionality can take several minutes to complete and is therefore separated from the root route to ensure that at least an initial home page loads quickly.
# The root route displays the current contents of a Mongo database using a Flask template (index.html) for styling. The scrape route activates a script 
# (scrape_mars.py) that scrapes the latest Mars mission images and facts from various websites and updates the Mongo database.
# Pymongo is needed to connect to the Mongo database.

# Import dependencies.
from flask import Flask, render_template
import pymongo

# Set up Flask app to run from command line.
app = Flask(__name__)

# Set up Mongo connection using Pymongo library.
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
# Connect to Mongo database and collection.
db = client.mars_db
mars_collection = db.mars_collection

# Root route queries Mongo database containing scraped content and passes results through a Flask html template before rendering.
@app.route('/')
def index():
    # Query collection and store results in a dictionary variable.
    latest_content = mars_collection.find_one()

    # Render dictionary via Flask template.
    return render_template("index.html", latest_content = latest_content)

# Scrape route activates scrape_mars.py to scrape a set of websites.
@app.route('/scrape')
def scrape():
    # Import local scrape_mars.py script
    import scrape_mars
    # Run scrape function and retreive dictionary of scraped content.
    post = scrape_mars.scrape()
    # Delete previous document from Mongo collection.
    mars_collection.delete_many({})
    # Post new document to Mongo collection.
    mars_collection.insert_one(post)
    # Call index() to present new content.
    return index()


# Set up Flask app to run from command line.
if __name__ == "__main__":
    app.run(debug=True)