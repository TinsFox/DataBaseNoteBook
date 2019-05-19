from flask import Blueprint, request, jsonify, make_response
import json
from common.libs.user.UserService import UserService
from common.libs.Helper import getCurrentDate
from common.models.User import User
from application import app, db
from sqlalchemy import or_

route_user = Blueprint('uer_page', __name__)

'''
需要在www.py进行加载
'''


@route_user.route("/login", methods=["GET", "POST"])
def login():
    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    if request.method == 'GET':
        return "login GET"
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名~!'
        # app.logger(login_name)
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -2
        resp['msg'] = '请输入正确的密码~~'
        return jsonify(resp)

    user_info = User.query.filter_by(login_name=login_name).first()
    print(user_info.nickname)
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名和密码~~'
        return jsonify(resp)
    # 加密
    # if user_info.login_pwd != USerService.genePwd(login_pwd, user_info.login_salt):
    #     resp['code'] = -1
    #     resp['msg'] = '请输入正确的用户名和密码~~!'
    #     return jsonify(resp)
    # resp['data.code'] = 200
    resp['code'] = 200
    resp['msg'] = '登录成功~~!'
    resp['data'] = {'nickname': user_info.nickname}
    response = make_response(json.dumps(resp))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], "%s#%s" % (UserService.geneAuthCode(user_info), user_info))
    # return response
    return jsonify(resp)


# 登出
# @route_user.route('/logout')
# def logout():
#     response = make_response()
#     response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
#     return response

@route_user.route("/show", methods=["GET"])
def show():
    resp_data = []
    query = User.query
    query.count()
    resp = {'code': 200, 'msg': '查询成功', 'data': {}}
    list = query.order_by(User.uid.desc()).all()
    for x in list:
        resp_data.append(x.to_json())
    # resp['data'] = {'list': list}
    # resp_data['list'] = list
    return jsonify(resp_data)


@route_user.route("/add", methods=["GET", "POST"])
# 新增加用户
def add():
    resp = {'code': 200, 'msg': '添加', 'data': {}}
    if request.method == 'GET':
        return jsonify(resp)
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    sex = req['sex'] if 'sex' in req else ''
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的姓名！'
        return jsonify(resp)
    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的手机号码！'
        return jsonify(resp)
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的登录名！'
        return jsonify(resp)
    if login_pwd is None or len(login_name) < 6:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的登录密码！'
        return jsonify(resp)

    has_in = User.query.filter(User.login_name == login_name).first()
    if has_in:
        resp['code'] = -1
        resp['msg'] = '该用户名已存在！'
        return jsonify(resp)
    model_user = User()
    model_user.nickname = nickname
    model_user.mobile = mobile
    model_user.login_name = login_name
    model_user.sex = sex
    model_user.login_salt = UserService.geneSalt()
    model_user.login_pwd = UserService.genePwd(login_pwd, model_user.login_salt)
    model_user.created_time = getCurrentDate()
    model_user.updated_time = getCurrentDate()
    db.session.add(model_user)
    db.session.commit()
    return jsonify(resp)


@route_user.route("/search", methods=["GET", "POST"])
# 模糊查询nickname/mobile
def search():
    resp = {'code': 200, 'msg': '模糊查询成功', 'data': {}}
    if request.method == 'GET':
        return jsonify(resp)
    query = User.query
    req = request.values
    if 's' in req:
        list = []
        rule = or_(User.nickname.ilike("%{0}".format(req['s'])), User.mobile.ilike("%{0}".format(req['s'])))
        info = query.filter(rule)
        for x in info:
            list.append(x.to_json())
        resp['data'] = {'list': list}
        return jsonify(resp)
