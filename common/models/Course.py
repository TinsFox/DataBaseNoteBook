# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from application import db


class Course(db.Model):
    __tablename__ = 'course'

    name = db.Column(db.String(10), nullable=False)
    cid = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    id = db.Column(db.BigInteger, primary_key=True)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    def to_json(self):
        return {
            'course_name': self.name,
            'course_cid': self.cid,
            'course_type': self.type,
            'course_credit': self.credit,
            'updated_time': self.updated_time,
            'created_time': self.created_time,
        }
