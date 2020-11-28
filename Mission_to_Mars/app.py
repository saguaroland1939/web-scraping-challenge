# This Flask app contains two routes that can be used independently to display scraped data from a database and to scrape new data as needed.
# The root route displays the current contents of a Mongo database while the scrape route activates a script that scrapes the latest Mars mission
# images and facts from various websites and updates the Mongo database. 

# Import dependencies.
from flask import Flask, render_template
import pymongo

# Set up Flask app to run from command line.
app = Flask(__name__)

# Root route queries Mongo database containing scraped content and passes results through a Flask html template before rendering.
@app.route('/')
def index():
    # Query collection and store results in a dictionary variable.
    latest_content = collection.find()
    # Render dictionary via Flask template.
    return render_template("index.html", latest_content = latest_content)

# Scrape route activates scrape_mars.py to scrape a set of websites.
@app.route('/scrape')
def scrape()
    # Set up Mongo connection using Pymongo library.
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    # Connect to Mongo database and collection.
    db = client.mars_db
    mars_collection = db.mars_collection
    # Import local scrape_mars.py script
    import scrape_mars
    # Run scrape function and retreive dictionary of scraped content.
    post = scrape_mars.scrape()
    # Delete previous document from Mongo collection.
    mars_collection.remove({})
    # Post new document to Mongo collection.
    mars_collection.insert_one(post)

# Set up Flask app to run from command line.
if __name__ == "__main__":
    app.run(debug=True)