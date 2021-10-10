#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from libs.configurations import Configuration


class SessionController(object):

    hostdb = Configuration.SQ_HOST
    dbname = Configuration.SQ_NAME
    drive = 'sqlite'


    def getEngine(self):
        try:
            return create_engine("{}:///{}".format(self.drive, self.dbname))
        except Exception as e:
            raise e


    def getSession(self):
        try:
            engine = self.getEngine()
            DBSession = sessionmaker(bind=engine, autoflush=True)
            session = DBSession()
            return session
        except Exception as e:
            raise e


    def __init__(self):
        super(SessionController, self).__init__()
