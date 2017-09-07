#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import url_for
from flask import render_template
from flask import session
from datetime import datetime
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent

    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer', '42')
    #return response

    name = None
    form = NameForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, %s</h1>' % name

    return render_template('user.html', name=name)

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

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    manager.run()
