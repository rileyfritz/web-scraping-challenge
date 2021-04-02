from flask import Flask, jsonify
from scrape_mars import scrape

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()





if __name__ == '__main__':
    app.run(debug=True)