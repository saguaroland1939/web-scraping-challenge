# This Flask app contains two routes that can be used independently to display scraped data from a database and to scrape new data as needed.
# The root route displays the current contents of a Mongo database while the scrape route activates a script that scrapes the latest Mars mission
# images and facts from various websites and updates the Mongo database. 

# Import dependencies.
from flask import Flask, render_template
import pymongo

# Set up Flask app to run from command line.
app = Flask(__name__)

# Set up Mongo connection.
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Connect to Mongo database and collection.
db = client.mars_db
collection = db.mars_collection

# Root route queries Mongo database containing scraped content and passes results through a Flask html template before displaying them.
@app.route('/')
def index():

    # Query collection and store results in variable.
    items = list(collection.find())
    return render_template("index.html", new_items = items)

# Scrape route activates scrape_mars.py to scrape latest content from the four websites.
@app.route('/scrape')
def scrape()

    # Remove old MongoDB data in preparation for a new scrape.

    import scrape_mars
    doc = scrape_mars.scrape()
    collection.insert_one(doc)

    # Insert scrape results into MongoDB.

    return

# Set up Flask app to run from command line.
if __name__ == "__main__":
    app.run(debug=True)