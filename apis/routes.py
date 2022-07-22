from flask import Blueprint
from apis.data_fetcher import GetJsonDataFromApi , GetDefaultPage  ,Get_Token,ModifyApi ,DeleteApi
from apis.run import RunProject 

api_blueprint = Blueprint('challenge', __name__)

# define the API resources
get_default_page_api = GetDefaultPage.as_view('get_default_page_api')
get_data_from_api = GetJsonDataFromApi.as_view('get_data_from_api')
run_project = RunProject.as_view('run_project')
get_token = Get_Token.as_view('get_token')
modify_api = ModifyApi.as_view('modify_api')
delete_api = DeleteApi.as_view('delete_api')

# add Rules for API Endpoints
# default route

api_blueprint.add_url_rule(
    '/apis/get_token',
    view_func = get_token,
    methods=['POST']
)
api_blueprint.add_url_rule(
    '/apis/modify',
    view_func = modify_api,
    methods=['POST']

)
api_blueprint.add_url_rule(
    '/apis/delete',
    view_func = delete_api,
    methods=['DELETE']

)
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

api_blueprint.add_url_rule(
    '/apis/get_data_from_api',
    view_func = get_data_from_api,
    methods=['GET']
)
