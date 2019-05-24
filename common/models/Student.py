# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


from application import db


class Student(db.Model):
    __tablename__ = 'student'

    uid = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    pwd = db.Column(db.String(32), nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    department = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    xh = db.Column(db.Integer, nullable=False)
    permission = db.Column(db.Integer, nullable=False)
