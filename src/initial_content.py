





InitContent = {
# this is setting file 's content 
	'setting':"""

## write by qingluan 
# this is a config file
# include db and debug , static path 

import motor 
from os import path
# here to load all controllers

from controller import *

# db engine 
db_engine = motor.MotorClient()

# static path 
static_path = "./static"


Settings = {
        'db':db_engine,
        'debug':True,
        'autoreload':True,
        'cookie_secret':'This string can be any thing you want',
        'static_path' : static_path,
    }


## follow is router

appication = tornado.web.Application([
                (r'/',IndexHandler),
                # add some new route to router
                ##<route></route>
                # (r'/main',MainHandler),
         ],**Settings)


# setting port 
port = 8080

if __name__ == "__main__":
	appication.listen(8080)
	tornado.ioloop.IOLoop.instance().start() 

""",

# this is base handler for all handler to inherited
	'BaseHandler':"""
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

""",


# this is handler 's template

	'handler':"""


class %sHandler(BaseHandler):
	
	def prepare(self):
		super(%sHandler,self).prepare()
		self.template = "template/%s.html"

	def get(self):
		return self.render(self.template,post_page="/%s")

	@tornado.web.asynchronous
	def post(self):
		# you should get some argument from follow 
		post_args = self.get_argument("some_argument")
		# .....

		# self.redirect()  # redirect or reply some content
		self.write("hello world")
	""",
	'html':"""
<!DOCTYPE html>
<html lang="en">
<head>      
    <meta charset="UTF-8">
    <title>%s</title>                                                        
</head>     
<body>      
           <p>%s</p> 
</body>     
</html>
	""",
	'main':"""
#!/usr/bin/python
## write by qingluan 
# just a run file 

import tornado.ioloop
from tornado.ioloop import IOLoop
from setting import  appication

if __name__ == "__main__":
	appication.listen(8080)
	tornado.ioloop.IOLoop.instance().start() 

	"""

}
