import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
import json
from settings import DB_NAME, DB_USER, DB_PASSWORD


database_name = DB_NAME
database_path = 'postgresql://{}:{}{}/{}'.format(DB_USER, DB_PASSWORD, '@localhost:5432', database_name)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


"""
Users

"""
class UserAccount(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    UserName = Column(String)
    Password = Column(String)
    Address = Column(String)
    items = db.relationship('Item', backref='user')

    def __init__(self, UserName, Password, Address, items):
        self.UserName = UserName
        self.Password = Password
        self.Address = Address

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'UserName': self.UserName,
            'Address': self.Address
            }

"""
Items

"""
class Item(db.Model):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    Category = Column(String)
    Description = Column(String)
    ImageLink = Column(String)
    StartingBid = Column(Integer)
    AuctionBeginingDate = Column(DateTime(timezone=True))
    AuctionEndingDate = Column(DateTime(timezone=True))
    user_id = Column(Integer, db.ForeignKey('users.id'))

    def __init__(self, title, Category, Description, ImageLink, StartingBid, AuctionBeginingDate, AuctionEndingDate, user_id):
        self.title = title
        self.Category = Category
        self.Description = Description
        self.ImageLink = ImageLink
        self.StartingBid = StartingBid
        self.AuctionBeginingDate = AuctionBeginingDate
        self.AuctionEndingDate = AuctionEndingDate

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
	    'Category': self.Category,
	    'Description': self.Description,
	    'ImageLink': self.ImageLink,
	    'StartingBid': self.StartingBid,
	    'AuctionBeginingDate': self.AuctionBeginingDate,
	    'AuctionEndingDate': self.AuctionEndingDate
            }
