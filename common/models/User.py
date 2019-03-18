# coding: utf-8
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from application import db
# db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(20))
    passwd = db.Column(db.String(10))
    sex = db.Column(db.String(255))
    departments = db.Column(db.String(255))
    permission = db.Column(db.INT)
    _class = db.Column('class', db.String(255))
