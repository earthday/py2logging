#!/usr/bin/env python

import cherrypy
import logging
import logging.config

# from logger import LOG_CONF
import yaml
import os

with open("logger.yaml") as f:
    LOG_CONF = yaml.safe_load(f.read())

logging.config.dictConfig(LOG_CONF)

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        logging.info("test")
        cherrypy.log("ccccccc")
        return "Hello World!"

cherrypy.quickstart(HelloWorld())
