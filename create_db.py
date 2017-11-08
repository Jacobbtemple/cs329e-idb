import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Base, Book, engine

# bind the engine to the base class. This makes the connection
# between our class definitions and the corresponding tables
# within our database
Base.metadata.bind = engine

# create session maker object to establish a link
# of communication between our code execution and
# the engine we just created
DBSession = sessionmaker(bind=engine)

# in order to create, read, update or delete information
# on our database, SQLAlchmey executes database operations
# via an interface called a session.
# A session allows us to write down all the commands
# we want to execute but not send them to the DB
# until we call "commit"
# create an instance of DBSession
session = DBSession()


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_book():
    books = load_json('books.json')
    for oneBook in books:
        try:
            google_id = oneBook['google_id']
            title = oneBook['title']
            try:
                isbn = oneBook['isbn']
            except:
                isbn = None
            try:
                publication_date = oneBook['publication_date']
            except:
                publication_date = None
            try:
                book_image_url = oneBook['image_url']
            except:
                book_image_url = None
            try:
                book_description = oneBook['description']
            except:
                book_description = None
            publishers = oneBook['publishers']
            authors = oneBook['authors']

            for onePublisher in publishers:
                try:
                    publisher_wikipedia_url = onePublisher['wikipedia_url']
                except:
                    publisher_wikipedia_url = None
                try:
                    publisher_name = onePublisher['name']
                except:
                    publisher_name = None
                try:
                    publisher_description = onePublisher['description']
                except:
                    publisher_description = None
                try:
                    owner = onePublisher['owner']
                except:
                    owner = None
                try:
                    publisher_image_url = onePublisher['image_url']
                except:
                    publisher_image_url = None
                try:
                    website = onePublisher['website']
                except:
                    website = None
            for oneAuthor in authors:
                try:
                    born = oneAuthor['born']
                except:
                    born = None
                try:
                    author_name = oneAuthor['name']
                except:
                    author_name = None
                try:
                    education = oneAuthor['education']
                except:
                    education = None
                try:
                    nationality = oneAuthor['nationality']
                except:
                    nationality = None
                try:
                    author_description = oneAuthor['description']
                except:
                    author_description = None
                try:
                    alma_mater = oneAuthor['alma_mater']
                except:
                    alma_mater = None
                try:
                    author_wikipedia_url = oneAuthor['wikipedia_url']
                except:
                    author_wikipedia_url = None
                try:
                    author_image_url = oneAuthor['image_url']
                except:
                    author_image_url = None
        except IntegrityError:
            pass

        newBook = Book(google_id=google_id, title=title, isbn=isbn, publication_date=publication_date, book_image_url=book_image_url,book_description=book_description, publisher_wikipedia_url=publisher_wikipedia_url,publisher_name=publisher_name, publisher_description=publisher_description, owner=owner, publisher_image_url=publisher_image_url, website=website, born=born, author_name=author_name, education=education, nationality=nationality, author_description=author_description, alma_mater=alma_mater, author_wikipedia_url=author_wikipedia_url, author_image_url=author_image_url)
        # After I create the book, I can then add it to my session.
        session.add(newBook)
        # commit the session to my DB.
        session.commit()

create_book()
