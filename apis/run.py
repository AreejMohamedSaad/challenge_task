from flask.views import MethodView
import json
from apis.data_fetcher import GetJsonDataFromApi as get_data
from apis import app, config

import os
class RunProject(MethodView):
      """
      Run project from this url (certain data from url )
      """
      def get(self):
            # get data from api and save it in a json file 
            data_from_api = get_data.get_data(self);
            # read json file and return data as string
            read_data = get_data.read_data_from_json_file(data_from_api)
            # data will be converted to list to be able to work on it 
            data_list = list(eval(read_data))
           
            return data_list
            