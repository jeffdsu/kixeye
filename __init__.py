#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_security.forms import RegisterForm
from flask_security.forms import Required
from wtforms import TextField

app = Flask(__name__, template_folder='static')

import kixeye.views

