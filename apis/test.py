  
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
        "name": "Admiral",
        "species": "Bird",
        "personality": "Cranky",
        "gender": "Male",
        "birthday": {
            "month": 1,
            "day": 27,
            "text": "January 27th"
        }
    },
    {
        "name": "Agent S",
        "species": "Squirrel",
        "personality": "Peppy",
        "gender": "Female",
        "birthday": {
            "month": 7,
            "day": 2,
            "text": "July 2nd"
        }
    },
    {
        "name": "Agnes",
        "species": "Pig",
        "personality": "Sisterly",
        "gender": "Female",
        "birthday": {
            "month": 4,
            "day": 21,
            "text": "April 21st"
        }
    },
    {
        "name": "Al",
        "species": "Gorilla",
        "personality": "Lazy",
        "gender": "Male",
        "birthday": {
            "month": 10,
            "day": 18,
            "text": "October 18th"
        }
    },
    {
        "name": "Alfonso",
        "species": "Alligator",
        "personality": "Lazy",
        "gender": "Male",
        "birthday": {
            "month": 6,
            "day": 9,
            "text": "June 9th"
        }
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
