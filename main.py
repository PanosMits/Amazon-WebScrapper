from flask import Flask, request, jsonify
from services.uk.amazon_uk_service import AmazonUkService
from services.us.amazon_us_service import AmazonUsService
import os

app = Flask(__name__)

amazonUkService = AmazonUkService()
amazonUsService = AmazonUsService()

@app.route('/search/url', methods=['POST'])
def searchByUrl():
    request_data = request.get_json()
    url = request_data['url']
    return amazonUkService.scrapByUrl(url)

@app.route('/search/title', methods=['POST'])
def searchByTitle():
    request_data = request.get_json()
    title = request_data['title']
    uk_amazon_results = amazonUkService.search(title)
    # us_amazon_results = amazonUsService.search(title)
    return jsonify({
        'uk_results': uk_amazon_results,
        # 'us_results': us_amazon_results
    })

if __name__ == "__main__":
    app.run(debug=True)
