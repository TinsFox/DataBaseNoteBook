# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from application import db


class OrderMessage(db.Model):
    __tablename__ = 'order_message'

    ISBN = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(20), nullable=False)
    teacher_name = db.Column(db.String(20), nullable=False)
    order_cout = db.Column(db.Integer, nullable=False)
    use_grade = db.Column(db.String(20), nullable=False)
    order_id = db.Column(db.String(20), primary_key=True)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    def to_json(self):
        return {
            'ISBN': self.ISBN,
            'course_name': self.course_name,
            'teacher_name': self.teacher_name,
            'order_cout': self.logiorder_coutn_pwd,
            'use_grade': self.use_grade,
            'updated_time': self.updated_time,
            'created_time': self.created_time,
            'order_id': self.order_id
        }
