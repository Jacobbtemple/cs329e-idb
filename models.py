'''
This file defines the models for a book
'''
# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship

# for configuring code at the end of the file
from sqlalchemy import create_engine


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know
# that our classes are special SQLAlchemy classes that
# corresponds to tables in our DB)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    google_id = Column(String(100), primary_key=True)
    title = Column(String(100), nullable=False)
    isbn = Column(String(100), nullable=False)
    publication_date = Column(String(100), nullable=False)
    image_url = Column(String(100), nullable = False)
    book_description = Column(String(100), nullable=False)
    publisher_wikipedia_url = Column(String(100), nullable=False)
    publisher_name = Column(String(100), nullable=False)
    publisher_description = Column(String(100), nullable=False)
    owner = Column(String(100), nullable=False)
    publisher_image_url = Column(String(100), nullable=False)
    website = Column(String(100), nullable=False)
    born = Column(String(100), nullable=False)
    author_name = Column(String(100), nullable=False)
    education = Column(String(100), nullable=False)
    nationality = Column(String(100), nullable=False)
    description = Column(String(3000), nullable=False)
    alma_mater = Column(String(100), nullable=False)
    author_wikipedia_url = Column(String(100), nullable=False)
    author_image_url = Column(String(100), nullable=False)
    



SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:19970131@localhost/mydb')
#MESSAGE FROM JEFF: TO RUN LOCALLY, CHANGE POSTGRES->YOUR USERNAME, CHANGE FRAIJ->YOUR PASSWORD, CHANGE BOOKS->YOUR DB NAME

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python database_setup.py
# you may receive the following error:
# ImportError: No module named 'psycopg2'
# This indicates that you need to install 'psycopg2' module
# To install the 'psycopg2' module:
# pip install psycopg2
