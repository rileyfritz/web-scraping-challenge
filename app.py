from flask import Flask, jsonify
import scrape_mars
from scrape_mars import scrape

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()
    mars_data = jsonify(mars_data)
    return mars_data

# print(mars_data)


if __name__ == '__main__':
    app.run(debug=True)