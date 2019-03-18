from flask import Blueprint, request, jsonify
from common.models.User import User
from common.libs.user.UserService import UserService

route_user = Blueprint('user_page', __name__)


@route_user.route("/login", methods=['GET', 'POST'])
def login():
    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    if request.method == "GET":
        # GET method
        # return render_template("user/login.html")
        return "login method='GET'"
    else:
        # POST method
        req = request.values
        user_id = req['user_id'] if 'user_id' in req else ''
        passwd = req['passwd'] if 'passwd' in req else ''

        if user_id is None or len(user_id) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名'
            return jsonify(resp)

        if passwd is None or len(passwd) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的密码'
            return jsonify(resp)

        user_info = User.query.filter_by(user_id=user_id)
        if not user_info:
            resp['code'] = -1
            resp['msg'] = '请输入正确的用户名和密码~~'
            print(user_info)
        # if user_info.passwd != UserService.genePwd(passwd, user_info.salt):
        #     resp['code'] = -2
        #     resp['msg'] = '请输入正确的密码~~'
        #     return jsonify(resp)
        else:
            resp['code'] = 200
            resp['msg'] = '登录成功!'
            return jsonify(resp)
    return "%s - %s" % (user_id, passwd)
