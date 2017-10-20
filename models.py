from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/tutorialdb'
db = SQLAlchemy(app)

class Heroes(db.Model):
    __tablename__ = 'heroes'
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(120), nullable=False)
    wiki = db.Column(db.String(120), nullable=False)
    #series = db.Column()

class Creators(db.Model):
    __tablename__ = 'creators'
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(120), nullable=False)
    comics = db.Column(db.String(80), nullable=False)
    #series = db.Column()

class Series(db.Model):
    __tablename__ = 'series'
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    startyear = db.Column(db.Integer, primary_key=True)
    endyear = db.Column(db.Integer, primary_key=True)
    #creators = db.Column()
    #characters = db.Column()

db.drop_all()
db.create_all()