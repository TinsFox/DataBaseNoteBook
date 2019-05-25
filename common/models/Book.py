# coding: utf-8
from sqlalchemy import Column, DateTime, Float, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from application import db


class Book(db.Model):
    __tablename__ = 'book'

    name = db.Column(db.String(20), nullable=False)
    ISBN = db.Column(db.String(32), primary_key=True)
    press = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float(10), nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    def to_json(self):
        return {
            'name': self.name,
            'ISBN': self.ISBN,
            'press': self.press,
            'author': self.author,
            'price': self.price,
            'updated_time': self.updated_time,
            'created_time': self.created_time,
        }
