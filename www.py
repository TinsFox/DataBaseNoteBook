# 引入控制器
from web.controllers.index import route_index
from application import app
from web.controllers.api import route_api
"""
蓝图
"""
app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(route_api, url_prefix='/api')