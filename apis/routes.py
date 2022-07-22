from flask import Blueprint
from apis.data_fetcher import GetJsonDataFromApi , GetDefaultPage 
from apis.run import RunProject 

api_blueprint = Blueprint('challenge', __name__)

# define the API resources
get_default_page_api = GetDefaultPage.as_view('get_default_page_api')
get_data_from_api = GetJsonDataFromApi.as_view('get_data_from_api')
run_project = RunProject.as_view('run_project')

# add Rules for API Endpoints
# default route
api_blueprint.add_url_rule(
    '/',
    view_func = get_default_page_api,
    methods=['GET']
)
api_blueprint.add_url_rule(
    '/apis/run',
    view_func = run_project,
    methods=['GET']
)

#################################################

api_blueprint.add_url_rule(
    '/apis/get_data_from_api',
    view_func = get_data_from_api,
    methods=['GET']
)
