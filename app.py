# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask
from flask import render_template # Import render_template function

app = Flask(__name__)


@app.route('/')  # URL for function (default for home page)
@app.route('/index')  # Secondary URL for function
def index():
    return render_template('index.html')  # located in templates/

@app.route('/heroes')
def heroes():
    return render_template('Heroes.html')


@app.route('/creators')
def creators():
    #dict = {'string1': 'Testing.', 'string2': 'Hello, World!'}
    #return render_template('page3.html', strings=dict)  # Example of argument passing to HTML template
    return render_template('Creators.html')

@app.route('/series')
def series():
    return render_template('Series.html')

@app.route('/heroes-dormammu')
def dormammu():
    return render_template('Dormammu.html')

@app.route('/creators-gurihiru')
def gurihiru():
    return render_template('Gurihiru.html')

@app.route('/series-100thanniversary')
def anniversary():
    return render_template('100thAnniversary.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
