# coding: utf-8
from flask import render_template
from app import app
import sys
sys.path.append("..")
import config


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/group1')
def group1():
    return render_template('swflow.html', groupname="group1",group=config.group1)
@app.route('/group2')
def group2():
    return render_template('swflow.html', groupname="group2",group=config.group2)
@app.route('/group3')
def group3():
    return render_template('swflow.html', groupname="group3",group=config.group3)
