import json
from models import db, Book



def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def create_char():
<<<<<<< HEAD
    characters = load_json('books.json')
=======
    characters = load_json('marvel-heroes.json')
>>>>>>> 7c0f3b87b19e6ce298d0402ff211a095e912e4b4

    for c in characters['Books']:
        title = oneBook['title']
        id = oneBook['id']

        newchar = Book(title=title, id=id)
        # After I create the book, I can then add it to my session.
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()


create_char()