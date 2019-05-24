# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


from application import db


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.BigInteger, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    login_name = db.Column(db.String(20), nullable=False)
    login_pwd = db.Column(db.String(32), nullable=False)
    login_salt = db.Column(db.String(32), nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    def to_json(self):
        return {
            'uid': self.uid,
            'nickname': self.nickname,
            'login_name': self.login_name,
            'login_pwd': self.login_pwd,
            'updated_time': self.updated_time,
            'created_time': self.created_time,
            'login_salt': self.login_salt
        }
