
## this is write by qingluan 
# just a inti handler 
# and a tempalte offer to coder

import tornado
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
	def prepare(self):
		self.db = self.settings['db']
	def get_current_user(self):
		return (self.get_cookie('user'),self.get_cookie('passwd'))
	def get_current_secure_user(self):
		return (self.get_cookie('user'),self.get_secure_cookie('passwd'))
	def set_current_seccure_user_cookie(self,user,passwd):
		self.set_cookie('user',user)
		self.set_secure_cookie("passwd",passwd)





class IndexHandler(BaseHandler):
	
	def prepare(self):
		super(IndexHandler,self).prepare()
		self.template = "template/Index.html"

	def get(self):
		return self.render(self.template,post_page="/Index")

	@tornado.web.asynchronous
	def post(self):
		# you should get some argument from follow 
		post_args = self.get_argument("some_argument")
		# .....

		# self.redirect()  # redirect or reply some content
		self.write("hello world")
	


class LoginHandler(BaseHandler):
	
	def prepare(self):
		super(LoginHandler,self).prepare()
		self.template = "template/Login.html"

	def get(self):
		return self.render(self.template,post_page="/Login")

	@tornado.web.asynchronous
	def post(self):
		# you should get some argument from follow 
		post_args = self.get_argument("some_argument")
		# .....

		# self.redirect()  # redirect or reply some content
		self.write("hello world")
	