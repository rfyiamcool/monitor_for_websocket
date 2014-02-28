# coding: utf-8
import os
from cgi import parse_qs, escape

from flask import Flask
from websocket import handle_websocket

app = Flask(__name__)
app.debug = True

def my_app(environ, start_response):  
    path = environ["PATH_INFO"]  
    if path == "/data":  
        handle_websocket(environ["wsgi.websocket"], parse_qs(environ['QUERY_STRING']).get('group',[''])[0])   
    else:  
        return app(environ, start_response)  

import views
