from web.controllers.api import route_api
from common.libs.Helper import getCurrentDate, getOrdreID
from flask import request, jsonify
from application import db, app
from common.models.OrderMessage import OrderMessage
from common.models.Book import Book


@route_api.route("order/add", methods=["GET", "POST"])
def OrderAdd():
    resp = {'code': 200, 'msg': '订购成功', 'data': {}}
    if request.method == 'GET':
        OrderID = getOrdreID()
        app.logger.info(len(str(OrderID)))
        return 'OrderID'.format({0}, OrderID)
    req = request.values
    course_name = req['course_name'] if 'course_name' in req else ''
    book_name = req['book_name'] if 'book_name' in req else ''
    teacher_name = req['teacher_name'] if 'teacher_name' in req else ''
    order_count = req['order_count'] if 'order_count' in req else ''
    user_grade = req['user_grade'] if 'user_grade' in req else ''
    app.logger.info(user_grade)
    if course_name is None or len(course_name) < 1 or teacher_name is None or len(
            teacher_name) < 1 or order_count is None or len(order_count) < 1 or user_grade is None or len(
        user_grade) < 1 or book_name is None or len(book_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的订单信息~!'
        return jsonify(resp)

    book_info = Book.query.filter_by(name=book_name).first()
    order_info = OrderMessage.query.filter_by(ISBN=book_info.ISBN).first()
    if order_info:
        resp['code'] = -2
        resp['msg'] = '已订购过此教材~~'
        return jsonify(resp)
    total_price = float(book_info.price) * float(order_count)
    model_order = OrderMessage()
    model_order.order_id = str(getOrdreID())
    model_order.course_name = course_name
    model_order.ISBN = book_info.ISBN
    model_order.teacher_name = teacher_name
    model_order.order_cout = order_count
    model_order.use_grade = user_grade
    model_order.total_price = str(total_price)
    model_order.created_time = getCurrentDate()
    model_order.updated_time = getCurrentDate()
    db.session.add(model_order)
    db.session.commit()
    return jsonify(resp)


@route_api.route("order/show", methods=["GET"])
def showOrder():
    resp_data = []
    query = OrderMessage.query
    query.count()
    resp = {'code': 200, 'msg': '查询成功', 'data': {}}
    list = query.order_by(OrderMessage.cid.desc()).all()
    for x in list:
        resp_data.append(x.to_json())
    resp['data'] = {'list': resp_data}
    return jsonify(resp)
