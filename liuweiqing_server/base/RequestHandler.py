#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: RequestHandler.py
@date: 16/3/17 下午6:20
"""

import tornado.web

class RequestHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(RequestHandler, self).__init__(*args, **kwargs)