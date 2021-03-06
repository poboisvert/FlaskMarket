#import sqlite3
from db import db

class MarketModel(db.Model):
    __tablename__ = 'markets'

    # Database variables
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    rating = db.Column(db.Float(precision=2))
    year = db.Column(db.Float(precision=2))
    describe = db.Column(db.String(80))
    baseURL = db.Column(db.String(80))
    channel = db.Column(db.String(80))

    def __init__(self, title, rating, year, describe, baseURL, channel):
        self.title = title
        self.rating = rating
        self.year = year
        self.describe = describe
        self.baseURL = baseURL
        self.channel = channel

    def json(self):
        return {'title': self.title, 'rating': self.rating, 'year': self.year, 'describe': self.describe, 'baseURL': self.baseURL, 'channel': self.channel}

    @classmethod
    def find_by_name(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
        #    return cls(*row)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        #  query = "INSERT INTO items VALUES(?, ?)"
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()