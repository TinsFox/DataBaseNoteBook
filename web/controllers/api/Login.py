from web.controllers.api import route_api
from flask import request, jsonify
from application import app
from common.models.User import User


@route_api.route("login/", methods=["GET", "POST"])
def use():
    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    if request.method == 'GET':
        return "login"
    req = request.values
    xh = req['xh'] if 'xh' in req else ''
    pwd = req['pwd'] if 'pwd' in req else ''
    app.logger.info(len(xh))
    if xh is None or len(xh) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名~!'
        return jsonify(resp)
    if pwd is None or len(pwd) < 1:
        resp['code'] = -2
        resp['msg'] = '请输入正确的密码~~'
        return jsonify(resp)
    login_info = User.query.filter_by(xh=xh).first()
    """
    SELECT *
    FROM student 
    WHERE student.xh = xh
    """
    if not login_info or login_info.pwd != pwd:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码~~'
        return jsonify(resp)

    # 返回表里信息的permission身份字段
    resp['data'] = {'permission': login_info.permission}
    return jsonify(resp)
