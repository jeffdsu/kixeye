#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask_security import UserMixin
from flask_security import RoleMixin
from flask_security.utils import encrypt_password
from flask_security.utils import verify_password
from kixeye import app
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from kixeye.database import Base
#pylint: disable=E1101


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    nickname = Column(String)
    wins = Column(Integer)
    losses = Column(Integer)
    currentWinStreak = Column(Integer)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    lastSeen = Column(DateTime, default=datetime.utcnow, nullable=False)

    @property
    def success(self):
        '''Return object data in serializeable format'''
        return {
            "error" : False,
            "time" : datetime.utcnow,
            "userid": self.id
        }

    @property
    def error(self):
        '''Return object data in serializeable format'''
        return {
            "error" : True,
            "time" : datetime.utcnow,
            "msg": "unknown user"
        }

