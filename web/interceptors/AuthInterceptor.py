# from application import app
# from flask import request
#
#
# @app.before_equest
# def before_equest():
#     path = request.path
#
#
# """
# 判断用户是否登录
# """
#
#
# def check_login():
#     cookies = request.cookies
#     auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config[
#                                                                  app.config['AUTH_COOKIE_NAME']] in cookies else ''
#     app.logger.info(auth_cookie)
