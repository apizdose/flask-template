#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
import socket

HOSTNAME = socket.gethostname()

try:
    CONTENT=os.environ["CONTENT"]
except: CONTENT='<br><br><center><h1> Need to define env var in .env file!'    

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return f'{CONTENT} {HOSTNAME}'
        
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
