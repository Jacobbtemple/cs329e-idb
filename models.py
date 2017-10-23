from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/tutorialdb'
db = SQLAlchemy(app)

class Books(db.Model):
    __tablename__ = 'books'
    title = db.Column(db.String(80), nullable=False)
    googleID = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(120), nullable=False)
    publicationDate = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

class Publishers(db.Model):
    __tablename__ = 'publishers'
    name = db.Column(db.String(80), nullable=False)
    wikiURL = db.Column(db.String(120), nullable=False)
    owner = db.Column(db.String(80), nullable=False)
    imageURL = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(120), nullable=False)

class Authors(db.Model):
    __tablename__ = 'authors'
    name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80), nullable=False)
    education = db.Column(db.String(80), nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    almaMater = db.Column(db.String(80), nullable=False)

db.drop_all()
db.create_all()