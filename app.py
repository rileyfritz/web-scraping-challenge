from flask import Flask, jsonify
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

    return f'done'

# @app.route('/')
# def homepage():



if __name__ == '__main__':
    app.run(debug=True)