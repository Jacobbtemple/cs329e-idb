from flask import Flask
from flask import render_template # Import render_template function

app = Flask(__name__)

@app.route('/')
def splash():
	return render_template('splash.html')

@app.route('/books')
def books():
	return render_template('books.html')

@app.route('/publishers')
def publishers():
	return render_template('publishers.html')

@app.route('/authors')
def authors():
	return render_template('authors.html')

@app.route('/books/sorcerersstone')
def sorcerersstone():
	return render_template('sorcerersstone.html')

@app.route('/publishers/pottermore')
def pottermore():
	return render_template('pottermore.html')

@app.route('/authors/jkrowling')
def jkrowling():
	return render_template('jkrowling.html')

@app.route('/authors/Heinlein')
def heinlein():
	return render_template('Heinlein.html')

@app.route('/books/Stranger')
def stranger():
	return render_template('Stranger.html')

@app.route('/publishers/Putnam')
def putnam():
	return render_template('Putnam.html')

@app.route('/books/thegodfather')
def thegodfather():
	return render_template('TheGodfather.html')

@app.route('/publishers/penguingroup')
def penguingroup(): 
	return render_template('PenguinGroup.html')

@app.route('/authors/mariopuzo')
def mariopuzo():
	return render_template('MarioPuzo.html')

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
