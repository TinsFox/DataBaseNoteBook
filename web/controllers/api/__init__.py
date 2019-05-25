from flask import Blueprint

route_api = Blueprint('api_page', __name__)
# 新增加的要在这里引入，否则404
from web.controllers.api.Member import *
from web.controllers.api.Login import *
from web.controllers.api.course import *
from web.controllers.api.book import *
from web.controllers.api.order import *


@route_api.route("/")
def index():
    return "Mina Api V1.0"
