from common.libs.Helper import getCurrentDate
from web.controllers.api import route_api
from flask import request, jsonify, json
from application import db, app
from common.models.Book import Book


@route_api.route("book/add", methods=["GET", "POST"])
def book():
    resp = {'code': 200, 'msg': '添加成功', 'data': {}}
    if request.method == 'GET':
        return "add Book"
    req = request.values
    name = req['name'] if 'name' in req else ''
    ISBN = req['ISBN'] if 'ISBN' in req else ''
    press = req['press'] if 'press' in req else ''
    author = req['author'] if 'author' in req else ''
    price = req['price'] if 'price' in req else ''
    # app.logger.info(len(name))
    if name is None or len(name) < 1 or press is None or len(press) < 1 or author is None or len(
            author) < 1 or price is None or len(price) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的书籍信息~!'
        return jsonify(resp)
    login_info = Book.query.filter_by(ISBN=ISBN).first()
    """
    SELECT *
    FROM book 
    WHERE book.ISBN = ISBN
    """
    if login_info:
        resp['code'] = -2
        resp['msg'] = '此书籍已存在~~'
        return jsonify(resp)
    model_book = Book()
    model_book.ISBN = ISBN
    model_book.name = name
    model_book.author = author
    model_book.price = price
    model_book.press = press
    model_book.created_time = getCurrentDate()
    model_book.updated_time = getCurrentDate()
    db.session.add(model_book)
    db.session.commit()
    # resp['data'] = {'permission': login_info.permission}
    return jsonify(resp)


@route_api.route("book/show", methods=["GET", "POST"])
def bookShow():
    resp = {'code': 200, 'msg': '查询成功', 'data': {}}
    resp_data = []
    query = Book.query
    query.count()
    list = query.order_by(Book.ISBN.desc()).all()
    for x in list:
        resp_data.append(x.to_json())
    resp['data'] = {'list': resp_data}
    return jsonify(resp)


@route_api.route("book/modify", methods=["GET", "POST"])
def modify():
    resp = {'code': 200, 'msg': '修改成功', 'data': {}}
    if request.method == 'GET':
        return "modify Book"
    req = request.values
    name = req['name'] if 'name' in req else ''
    ISBN = req['ISBN'] if 'ISBN' in req else ''
    press = req['press'] if 'press' in req else ''
    author = req['author'] if 'author' in req else ''
    price = req['price'] if 'price' in req else ''
    if name is None or len(name) < 1 or press is None or len(press) < 1 or author is None or len(
            author) < 1 or price is None or len(price) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的书籍信息~!'
        return jsonify(resp)
    book_info = Book.query.filter(Book.ISBN == ISBN).first()
    app.logger.info(book_info.updated_time)
    if book_info:
        model_book = book_info
        model_book.ISBN = ISBN
        model_book.name = name
        model_book.author = author
        model_book.price = price
        model_book.press = press
        model_book.updated_time = getCurrentDate()
    db.session.add(model_book)
    db.session.commit()
    return jsonify(resp)
