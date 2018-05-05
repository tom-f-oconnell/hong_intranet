#!/usr/bin/env python3

"""
For viewing and doing light exploration on my behavioral data in Betty Hong's
lab. Maybe other types of data in the future.
"""

import socket
import sqlite3

from flask import Flask
from flask import render_template
from flask import abort

app = Flask(__name__)

# either locally or on NAS. could also just config paths via file / env vars
locally = True

# TODO periodically search for files matching description outside of specified
# directories? maybe as a separate process?

#def lab_members():
#    """Returns list of lab members from hidden YAML file in NAS root."""

@app.route('/')
def index():
    people = {'Kristina', 'Tom'}
    return render_template('index.html', host=socket.gethostname())

# will I need to not have a variable string at the top level? will it prevent me
# from making other routes at this level? (then do /people/<person> or
# something)
# TODO also need to check the name is valid though... how do i want to store
# names and metadata associated with them?
@app.route('/<name>')
def lab_member(name):
    if not name in lab_members:
        
    return render_template('lab_member.html', name=name)

@app.route('/tafc_small')
def tafc_small_experiments(experiment_id):
    return render_template('experiments.html',
        setup_name="Tom's two-alternative forced choice setup")

# TODO abstract tafc_small into a <apparatus> or <setup> variable? validation?
@app.route('/tafc_small/<experiment>')
def tafc_small_experiment(experiment):
    return render_template('tafc_small.html')

@app.route('/tafc_small/<experiment>/<replicate>')
def tafc_small_experiment(experiment, replicate):
    return render_template('tafc_small.html')

# TODO use html5 video stuff to crop parent video to roi of fly
@app.route('/tafc_small/<experiment>/<replicate>/<roi>')
def tafc_small_experiment_roi(experiment, replicate, roi):
    return render_template('tafc_small.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
