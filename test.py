#! /usr/bin/env python

from chunker import *
from flask import Flask
from flask import request

try:
   import simplejson as json
except ImportError:
   import json

app = Flask(__name__)
chunker = TagChunker(get_iob_chunker())

@app.route('/')
def index():
    text = request.args.get('text', '')
    return json.dumps(chunker.chunk(text))

app.run(debug=True)
