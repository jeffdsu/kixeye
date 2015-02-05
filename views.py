#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import mimetypes

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import jsonify
from flask import abort
from flask.ext.login import current_user
from flask_security import login_required

from kixeye import app
from kixeye.models import User
#pylint: disable=E1101



### ROUTES ###
@app.route('/')
#@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/users', methods=['POST'])
@app.route('/users/<int:user_id>', methods=['POST'])
def update_user(user_id=None):
    '''
    Update user settiings
    '''
    user = _get_user(user_id)
    data = request.json
    if not data:
        abort(400, 'No data to update')

    first_name = data.get('firstname', None)
    last_name = data.get('lastname', None)
    location = data.get('location', None)
    birthday = data.get('birthday', None)

    params = {
        'firstname': first_name,
        'lastname': last_name,
        'location': location,
        'birthday': birthday
    }
    kwargs = dict((k, v) for k, v in params.iteritems() if v is not None)
    user.update(**kwargs)
    return wrap_success_response(user.serialize)
