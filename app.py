from flask import Flask, jsonify, render_template, redirect
import scrape_mars
from scrape_mars import scrape
import pymongo

app = Flask(__name__)


@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    # Declare the database
    db = client.mars_db
    # Declare the collection
    facts = db.facts
    facts.update({},mars_data, upsert=True)

    return redirect('/')

@app.route("/")
def index():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    mars_data = db.facts.find_one()
    return render_template("index.html", mars_data=mars_data)



if __name__ == '__main__':
    app.run(debug=True)