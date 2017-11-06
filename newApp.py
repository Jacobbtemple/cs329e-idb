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
def author_template(name):
	info = session.query(Author).filter_by(name=name)
	birthday = info.birthday.first() #Depends on table call name
	education = info. education.first() #Depends on table call name
	nationality = info.nationality.first() #Depends on table call name
	about = info.about.first() #Depends on table call name
	school = info.school.first() #Depends on table call name
	wiki = info.wiki.first() #Depends on table call name
	image = info.wiki.first() #Depends on table call name
	books = info.books #Depends on table call name
	return render_template('author_template.html', name=name, birthday=birthday, education=education, nationality=nationality, about=about, school=school, wiki=wiki, image=image, books=books)

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
