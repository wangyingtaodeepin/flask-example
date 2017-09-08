#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm
from datetime import datetime

@main.route('/', methods=['GET', 'POST'])
def index():
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent

    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer', '42')
    #return response

    name = None
    form = NameForm()

    if form.validate_on_submit():
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks like you have changed your name!')

        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                        'mail/new_user', user=user)
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))

    return render_template('index.html', form=form, name=session.get('name'),
            known=session.get('known', False), current_time=datetime.utcnow())
