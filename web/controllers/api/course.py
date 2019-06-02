from web.controllers.api import route_api
from common.libs.Helper import getCurrentDate
from flask import request, jsonify, json
from application import db, app
from common.models.Course import Course


@route_api.route("course/add", methods=["GET", "POST"])
def course():
    resp = {'code': 200, 'msg': '添加成功', 'data': {}}
    if request.method == 'GET':
        return "add course"
    req = request.values
    name = req['name'] if 'name' in req else ''
    cid = req['cid'] if 'cid' in req else ''
    type = req['type'] if 'type' in req else ''
    credit = req['credit'] if 'credit' in req else ''
    if name is None or len(name) < 1 or cid is None or len(cid) < 1 or type is None or len(
            type) < 1 or credit is None or len(credit) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的书籍信息~!'
        return jsonify(resp)
    course_info = Course.query.filter_by(cid=cid).first()
    if course_info:
        resp['code'] = -2
        resp['msg'] = '课程已存在~~'
        return jsonify(resp)

    model_course = Course()
    model_course.name = name
    model_course.cid = cid
    model_course.type = type
    model_course.credit = credit
    model_course.created_time = getCurrentDate()
    model_course.updated_time = getCurrentDate()
    db.session.add(model_course)
    db.session.commit()
    return jsonify(resp)


@route_api.route("course/show", methods=["GET"])
def showCourse():
    resp_data = []
    query = Course.query
    query.count()
    resp = {'code': 200, 'msg': '查询成功', 'data': {}}
    list = query.order_by(Course.cid.desc()).all()
    for x in list:
        resp_data.append(x.to_json())
    resp['data'] = {'list': resp_data}
    return jsonify(resp)
