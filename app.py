from flask import Flask, jsonify
import scrape_mars
from scrape_mars import scrape
import pymongo

app = Flask(__name__)


@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()
    # mars_data = jsonify(mars_data)

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    # Declare the database
    db = client.mars_db
    # Declare the collection
    facts = db.facts
    # article = mars_data['first_article']
    facts.update({},mars_data, upsert=True)
    # db.update({}, mars_data, upsert=True)
    
    # results = facts.find()
    # for result in results:
    #     print(result)

    return f'{mars_data}'

# @app.route('/')
# def homepage():



if __name__ == '__main__':
    app.run(debug=True)