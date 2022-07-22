  
from audioop import reverse
from typing import List, Tuple
import json
from bcrypt import re
# import main Flask class and request object
from flask import Flask, request
from numpy import array
import operator, itertools
from collections import Counter
from flask import Flask, request

import requests

# create the Flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def read_data_from_json_file(filepath):
          f = open(filepath)
          # load the json data
          items = json.loads(f.read())
          f.close()
          print(items)

      # convert list to str dict type to be allowed return value
          str_response = json.dumps(items)
          return (str_response)

def get_data(data):
    json_data = json.dumps(data) 
    return json_data 
# def get_addres_api(longitude , latitude):


data = [
    {
        "id": 108,
        "name": "Zohannesgasse",
        "status": "true",
        "description": "Ecke Lichtenfelsgasse U2 Station Rathaus",
        "free_bikes": 5,
        "longitude": 16.356581,
        "latitude": 48.211433,
        "internal_id": 1026,
        "boxes": 30, 
        "free_boxes": 29
    },
    {
        "id": 109,
        "name": "Friedrich",
        "status": "true",
        "description": "Parkring / Stadtpark beim Haupteingang des Kursalons",
        "free_bikes": 5,
        "longitude": 16.376719,
        "latitude": 48.203366,
        "internal_id": 1029,
        "boxes": 30, 
        "free_boxes": 29
    },
    {
        "id": 112,
        "name": "Ring",
        "status": "false",
        "description": "Ecke Akademiestra\u00dfe in der Mitte der beiden Einkaufszentren der Ringstra\u00dfengalerien",
        "free_bikes": 2,
        "longitude": 16.371317,
        "latitude": 48.202157,
        "internal_id": 1028,
        "boxes": 30,
        "free_boxes": 29
    }
    ]



filepath = "apis/filename.json"

@app.route('/read_from_json_file-example')
def read_from_json_file_example():
    return read_data_from_json_file(filepath)

@app.route('/get_data')
def get_data_example():
    return get_data(data)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
