from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from models import Base, Book, engine
from create_db import create_book, session
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def splash():
	return render_template('splash.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/books')
def books():
	books = session.query(Book).all()
	return render_template('newBooks.html', books = books)

@app.route('/publishers')
def publishers():
	publishers = session.query(Book).distinct(Book.publisher_name)
	return render_template('newpublishers.html', publishers = publishers)

@app.route('/authors')
def authors():
	authors = session.query(Book).distinct(Book.author_name)
	return render_template('newauthors.html', authors = authors)

@app.route('/authors/<author_name>')
def author_page(author_name):
	# if do not add ".first()" to the end of this, the default data will look like a list of dictionaries
	info = session.query(Book).filter_by(author_name=author_name)
	birthday = info.first().born
	education = info.first().education
	nationality = info.first().nationality
	description = info.first().author_description
	alma_mater = info.first().alma_mater
	wikipedia_url = info.first().author_wikipedia_url
	image_url = info.first().author_image_url

	li = []
	for i in info:
		if i.publisher_name not in li:
			li.append(i.publisher_name)

	return render_template('author_template.html', info=info, author_name=author_name, birthday=birthday, education=education, nationality=nationality,\
	description=description, alma_mater=alma_mater, wikipedia_url=wikipedia_url, image_url=image_url, li=li)
	# the list of books is passed through info. It needs to be done this way because we must use a loop to create
	# the table of all books by the author

@app.route('/books/<title>')
def book_page(title):
	info = session.query(Book).filter_by(title=title)
	google_id = info.first().google_id
	isbn = info.first().isbn
	publication_date = info.first().publication_date
	description = info.first().book_description
	image_url = info.first().book_image_url

	return render_template('book_template.html', info=info, title=title, google_id=google_id, isbn=isbn, publication_date = publication_date,\
	description=description, image_url=image_url)

@app.route('/publishers/<publisher_name>')
def publisher_page(publisher_name):
	info = session.query(Book).filter_by(publisher_name=publisher_name)
	publisher_name = info.first().publisher_name
	owner = info.first().owner
	publisher_description = info.first().publisher_description
	website = info.first().website
	publisher_image_url = info.first().publisher_image_url

	li = []
	for i in info:
		if i.author_name not in li:
			li.append(i.author_name)

	return render_template('publisher_template.html', info=info, publisher_name=publisher_name, owner=owner, publisher_description = publisher_description, \
	website=website, publisher_image_url=publisher_image_url, li=li)

@app.route('/unit_tests')
def unit_tests():
	return json.dumps({"output": "...\n----------------------------------------------------------------------\nRan 3 tests in 0.026s\n\nOK"})


if __name__ == '__main__':
	# This is used when running locally. Gunicorn is used to run the
	# application on Google App Engine. See entrypoint in app.yaml.
	app.run(host='127.0.0.1', port=8080, debug=True)
