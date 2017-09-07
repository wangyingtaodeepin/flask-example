#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import url_for
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent

    response = make_response('<h1>This document carries a cookie!</h1>')

    response.set_cookie('answer', '42')

    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name

@app.route('/redirectTest')
def redirectTest():
    return redirect(url_for('index'))

@app.route('/abortTest')
def abortTest():
    abort(404)
    return '<h1>Hello</h1>'

@app.route('/make_responseTest')
def make_responseTest():
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    manager.run()
