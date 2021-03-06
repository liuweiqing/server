#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: SignUp.py
@date: 16/3/15 下午4:58
"""

import string
import random
import os
from tornado import gen
from rong import ApiClient
from RequestHandler import RequestHandler
from behaviors import CreatNewUser
from behaviors import CreatUserToken
import error
from bson.objectid import ObjectId
import logging


class SignUp(RequestHandler):

	@gen.coroutine
	def post(self, *args, **kwargs):
		mobile = self.get_argument('mobile')
		password = self.get_argument('password')

		flag = yield CreatNewUser().Action(mobile, password)
		if not flag:
			raise error.AccountAlreadyExists()
		account = yield self.user_model.GetUserFromMobile(mobile)
		uid = str(account['_id'])
		rongyun_token = self.application.rong_client.user_get_token(
			uid,
			account['nike_name'],
			'http://7xpt10.com1.z0.glb.clouddn.com/default.png'
		)

		server_token = ''.join([random.choice(string.digits + string.letters) for _ in range(32)])
		tid = yield CreatUserToken().Action(uid, server_token, rongyun_token['token'])
		print tid
		token_result = yield self.token_model.GetTokenFromTid(tid)
		print token_result['server_token']
		result = {
			'_id':str(account['_id']),
			'nike_name':account['nike_name'],
			'server_token':token_result['server_token'],
			'token':token_result['rongyun_token'],
			'avatar':account['avatar'],
			'unique_name':account['unique_name'],
			'sex':account['sex'],
			'signature':account['signature']
		}

		self.render(result)


"""
redis存储的数据
1 密码
2 token
3 session
"""




