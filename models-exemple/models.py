import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.obspath(os.path.dirname(__file__))

app = Flas(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Cat(db.Model):

    __tablename__ = 'cats'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    # one to many
    # Cats to many Toys...
    toys = db.relationship('Toy',backref='cat',lazy= 'dynamic')
    #ONE TO ONE
    #ONE PUPPY --- ONE OWNER
    owner = db.relationship('Owner',backref='cat',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Cat name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Cat name is {self.name} and no owner yet!"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name

class Toy(db.Model):

    __tablename__= 'toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Columns(db.Text)
    cat_id = db.Column(db.Integer,db.ForeignKey('cats.id'))

    def __init__(self, item_name,cat_id):
        self.item_name = item_name
        self.cat_id = cat_id


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Interger,primary_key=True)
    name = db.Column(db.Text)

    cat_id = db.Column(db.Integer,db.ForeignKey('cats.id'))

    def __init__(self,name,cat_id):
        self.name = name
        self.cat_id = cat_id
