#!/usr/bin/env python3

"""
For viewing and doing light exploration on my behavioral data in Betty Hong's
lab. Maybe other types of data in the future.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

# either locally or on NAS. could also just config paths via file / env vars
locally = True

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
