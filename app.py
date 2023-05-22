import os

import flask
from flask import Flask, render_template
import requests

app = flask.Flask(__name__)
apikey = "kXpcrQtK8a8ufxPLTD6BgMSzfR3lbVRTXlZ0tMxD"
baseurl = "https://api.nasa.gov/planetary/"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/astronomyPicOftheDay', methods=['GET'])
def my_form_post():
    api_url = baseurl + "apod?api_key=" + apikey
    response = requests.get(api_url)
    result = response.json()
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.getenv('PORT', 4444)), debug=True)
