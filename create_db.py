import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment
from sqlalchemy.orm import sessionmaker
from models import Base, Book, engine, Publisher, Author

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

def create_books():

    book = load_json('books.json')

    for oneBook in book['Books']:
        title       = oneBook['title']
        google_id   = oneBook['google_id']
        isbn        = oneBook['isbn']
        pub_date    = oneBook['publication_date']
        img_url     = oneBook['image_url']
        description = oneBook['description']
        publisher   = oneBook['publisher'][0]['name'] # needs to be changed
        author      = oneBook['author'][0]['name']

        for publisher in oneBook['publishers']:
            wikipedia_url = publisher["wikipedia_url"]
            name          = publisher["name"]
            description   = publisher["description"]
            owner         = publisher["owner"]
            image_url     = publisher["image_url"]
            website       = publisher["website"]

            # modify the argument names as needed for the database class
            newPublisher = Publisher(wiki_Url    = wikipedia_url
                                     name        = name
                                     description = description
                                     owner       = owner
                                     image_url   = image_url
                                     website     = website
                                    )

            session.add(newPublisher)
            session.commit() # unsure if needed or one at the very end

        for author in oneBook['authors']:
            born          = author["born"]
            name          = author["name"]
            education     = author["education"]
            nationality   = author["nationality"]
            description   = author["description"]
            alma_mater    = author["alma_mater"]
            wikipedia_url = author["wikipedia_url"]
            image_url     = author["image_url":]

            # modify the argument names as needed for the database class
            newAuthor = Author(born          = born
                               name          = name
                               education     = education
                               nationality   = nationality
                               description   = description
                               alma_mater    = alma_mater
                               wikipedia_url = wikipedia_url
                               image_url     = image_url
                               )

            session.add(newAuthor)
            session.commit() # unsure if needed here or one at the very end

        # modify the argument names as needed for the database class
        newBook = Book(title       = title,
                       id          = google_id,
                       isbn        = isbn,
                       pub_date    = pub_date,
                       img_url     = img_url,
                       description = description
                       publisher   = publisher
                       )

        session.add(newBook)

        session.commit() # unsure if needed

    session.commit() # unsure if needed or one after each book/author/publisher

create_books()
