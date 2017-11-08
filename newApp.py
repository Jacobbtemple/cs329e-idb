from flask import Flask
from flask import render_template # Import render_template function

app = Flask(__name__)

@app.route('/')
def splash():
	return render_template('splash.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/books')
def books():
	return render_template('books.html')

@app.route('/publishers')
def publishers():
	return render_template('publishers.html')

@app.route('/authors')
def authors():
	return render_template('authors.html')

@app.route('/authors/<name>')
def author_page(name):
	info = session.query(books).filter_by(authors=name)
	birthday = info.birthday.first() #Depends on table call name
	education = info.education.first() #Depends on table call name
	nationality = info.nationality.first() #Depends on table call name
	description = info.description.first() #Depends on table call name
	alma_mater = info.alma_mater.first() #Depends on table call name
	wiki_url = info.wiki_url.first() #Depends on table call name
	image_url = info.image_url.first() #Depends on table call name
	books = info.books #Depends on table call name
	return render_template('author_template.html', name=name, born=born, education=education, nationality=nationality, description=description, alma_mater=alma_mater, author_wikipedia_url=author_wikipedia_url, author_image_url=author_image_url, books=books)

@app.route('/books/<title>')
def author_page(title):
	#todo, test authors first

@app.route('/publishers/<publisher>')
def author_page(publisher):
	#todo, test authors first

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
