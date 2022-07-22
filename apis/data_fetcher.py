import requests
from flask.views import MethodView
import json
from apis import app, config


class GetDefaultPage(MethodView):
      """
      Defult page appears when default url is typed
      """
      def get(self):
            msg = "Welcome in Home page " 
            return  msg 

class GetJsonDataFromApi(MethodView):
    """
    Get Json Data From Api url
    """
    def get_data(self):
      params = {
        'api_key': '{API_KEY}',
      }
      r = requests.get(
          config.BASE_URL,
          params=params)
      response = r.content

      # decode the byte to list 
      decode_response = json.loads(response.decode('utf-8')) #type list 

      # convert list to sr dict type to be allowed return value
      str_response = json.dumps(decode_response) #type str

      filepath = config.filepath2

      # create json file 
      json_object = json.dumps(decode_response, indent = 4)
        
      # Writing to sample.json
      with open(filepath, "w") as outfile:
          outfile.write(json_object)
      return filepath
      # str_response

    def read_data_from_json_file(filepath):
          f = open(filepath)
          # load the json data
          items = json.loads(f.read())
          f.close()
      # convert list to str dict type to be allowed return value
          str_response = json.dumps(items)
          return (str_response)


