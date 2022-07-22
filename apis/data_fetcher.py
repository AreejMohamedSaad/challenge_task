from codecs import strict_errors
from django.test import client
from django.urls import conf
from flask_login import confirm_login
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

class Get_Token(MethodView):
    def post(self):
          body = {
            'client_id':"7ee095af-318a-4cd0-9e95-4a2fa8ccf34d",
            'client_secret' : "3618d70a25e1e5c39c4b72a311436b7b",
            'grant_type':config.grant_type
          }
         
          header = {'Content-Type': 'application/x-www-form-urlencoded'}
          r = requests.post(
          config.Token_URL ,data=body ,headers= header)
          print(r)
          token = r.content 
          print(token)
          return token


class ModifyApi(MethodView):

    def post(self):
        filepath = config.filepath2
        f = open(filepath)
          # load the json data
        items = json.loads(f.read())
        f.close()
        
        items["new_add"]=   {
        "new_page": 1,
        "new_next_page": 'null',
        "new_prev_page": 'null',
        "new_total_count": 1,
        "new_total_pages": 1
    }
        return items

class DeleteApi(MethodView):
      def delete(self):
        filepath = config.filepath2
        f = open(filepath)
          # load the json data
        items = json.loads(f.read())
        f.close()
        
        for key in items.copy():
              if key == "meta":
                    del items["meta"]
              
        return items
      
      
class GetJsonDataFromApi(MethodView):
    """
    Get Json Data From Api url
    """
    data = []
    def get(self):
      payload={}
      headers = {
        'X-Organization-Id': '5807769d-1c69-43a8-9850-045cb821f39f',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJKMjJlMmxLRUJxTGxXSjBkdjItT3JQdWxrRmFxbmdCUnhoRW1Hb2h1dnc4In0.eyJleHAiOjE2NTg1MDcwNTgsImlhdCI6MTY1ODQ5MjY1OCwianRpIjoiZDhkNTk3YzktZWYwYy00Yjc2LTgxMTUtZjQ0MTE4NGQ3MmRjIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLXN0YWdpbmcub25saW0uY29tL2F1dGgvcmVhbG1zL29ubGltIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjViYmFhYjU2LWViNzktNGM3My04MjRlLWY1NGQ5ODE1NTUzNSIsInR5cCI6IkJlYXJlciIsImF6cCI6IjdlZTA5NWFmLTMxOGEtNGNkMC05ZTk1LTRhMmZhOGNjZjM0ZCIsImFjciI6IjEiLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjbGllbnRJZCI6IjdlZTA5NWFmLTMxOGEtNGNkMC05ZTk1LTRhMmZhOGNjZjM0ZCIsImNsaWVudEhvc3QiOiIyYTAyOjgzODg6OGIwMDo1ZDgwOmI1NzY6MmUwMjoyY2Q6ZjQ5ZCIsInByZWZlcnJlZF91c2VybmFtZSI6InNlcnZpY2UtYWNjb3VudC03ZWUwOTVhZi0zMThhLTRjZDAtOWU5NS00YTJmYThjY2YzNGQiLCJjbGllbnRBZGRyZXNzIjoiMmEwMjo4Mzg4OjhiMDA6NWQ4MDpiNTc2OjJlMDI6MmNkOmY0OWQifQ.IGH5zkTRkb7hZDNp5Nw7MPLa024TDMibPqXnZDJQEj9W9HQobJdnsbEeHiTAAGCHjAfQDFfburDdWJJ7QqgEWSLOppBAPX-uZQSPjz86-8QCPZ0MrpF1Cg_kRnnZnspTGtG5B4MyLi8FDpI4vGd-QOVC6Kyoy-wnhDuADToiFXBItAY4I4wz35KUqSfko_2gbwGr64HvE1d2ZQVDtVYZ70dCGpY30W4EiLp1cXk_QfkC5VscVKu6caCLKLnVK_ajcasKzAFTsPdFEfTshvofxokAh8daA2X5KGXi2FxnwtIh7-ukQjJ_qOVJdhqxuYtbIKVDkPOfDW4hEB2i53ZtJQ'
      }

      response = requests.request("GET", config.url, headers=headers, data=payload)
    
      filepath = config.filepath2
      data = response.content
      # Writing to sample.json
      with open(filepath, "w") as outfile:
          outfile.write(response.text)

      
      return filepath


    def read_data_from_json_file(filepath):
          f = open(filepath)
          # load the json data
          items = json.loads(f.read())
          f.close()
      # convert list to str dict type to be allowed return value
          return items
          # (str_response)
