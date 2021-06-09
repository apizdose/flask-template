#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
import socket

hostname = socket.gethostname()

try:
    ENVIR=os.environ["ENVIR"]
except: ENVIR='<br><br><center><h1> Need to define env var in .env file!'    

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return f'{ENVIR} {hostname}'
        
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
