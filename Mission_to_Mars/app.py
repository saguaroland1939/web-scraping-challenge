# This Flask app contains two routes that can be used independently to display scraped data from a database and to scrape new data as needed.
# The root route displays the current contents of a Mongo database while the scrape route activates a script that scrapes the latest Mars mission
# images and facts from various websites and updates the Mongo database. 

# Import dependencies.
import scrape_mars
from flask import Flask, render_template

# Set up Flask app to run from command line.
app = Flask(__name__)

# Root route queries Mongo database containing scraped content and passes results through a Flask html template before displaying them.
@app.route('/')
def view():
    return render_template("index.html", dict=___)

# Scrape route activates scrape_mars.py to scrape latest content from the four websites.
@app.route('/scrape')
def scrape()
    scrape_mars.scrape()
    return

# Set up Flask app to run from command line.
if __name__ == "__main__":
    app.run(debug=True)