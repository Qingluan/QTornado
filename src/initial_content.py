





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
#this is a extends templates  , '$' is special syn , need to take a transation to '%' 
	'html':"""

<!DOCTYPE html>
<html lang="en">
<head>      
    <meta charset="UTF-8">
    <title>%s</title>     
    <link href="/static/bootstrap/dist/css/bootstrap.css" rel="stylesheet"></link>
    {$ block head_css $}
     <link href="/static/css/%s.css" rel="stylesheet"></link>
    {$ end $}
    {$ block extends_css $}
    {$ end $}
</head>     
<body>      
        <p>%s</p> 
        <script src="/static/jquery/dist/jquery.min.js"></script>
        <script src="/static/bootstrap/dist/js/bootstrap.js"></script>
        {$ block body_js $}
        <script src="/static/js/%s.js"></script>
        {$ end $}
        {$ block extends_js $}
        {$ end $}
</body>     
</html>
	""",
        'css':"""
#written by qingluan
#
#this css file is belong to %s
        """,
#this is a extends templates  , '$' is special syn , need to take a transation to '%' 
'extends_html':"""
{$ extends "%s.html"  $} 
    {$ block extends_css $}
        <link href="/static/css/%s.css" rel="stylesheet"></link>
    {$ end  $}

    {$ block extends_js $}
    <script src="/static/js/%s.js"></script>
    {$ end $}
{$ end $}
        """,
        'js':"""
        // this is js file for %s 
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

	""",
#this is a ad for our ISC 

        'ISC':"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="static/bootstrap/dist/css/bootstrap.css"></link>
            <title>{}</title>
                
                    <style type="text/css">
                        b{
                                font-weight: lighter;
                                    }
                                        h1,h3,h4 ,h2,h5{
                                                font-weight: 100;
                                                    }
                                                        .good-words{
                                                                margin-top: 20%;
                                                                    }
                                                                        </style>
                                                                        </head>
                                                                        <body>
                                                                        <div class="pic">
                                                                            <img src="static/images/hat.png" style="position: absolute;
                                                                            left: 25%;
                                                                            max-width: 200px;
                                                                            bottom: 41%;
                                                                            padding: 15px;
                                                                            border-right: solid 1px;">
                                                                            </div>
                                                                                <div class="container" style="position: absolute;
                                                                                bottom: 3%; margin-left: 20px">

                                                                                        <p style="font-weight: 100;
                                                                                        font-size: 15px;">Address: <small style="font-family: fantasy;" >113</small></p>   
                                                                                                <p style="font-weight: 100;
                                                                                                font-size: 15px;">Time: <small style="font-family: fantasy;">21:42</small></p>   
                                                                                                    </div>
                                                                                                        <div class="col-md-4" style="bottom: 33%;
                                                                                                        position: absolute;
                                                                                                        text-align: center;

                                                                                                        right: 31%;font-weight: 100">
                                                                                                                <div class="theme-main" style="
                                                                                                                text-align: left;
                                                                                                                margin-left: 11%;
                                                                                                                        ">
                                                                                                                                    <h1>ISA  </h1>
                                                                                                                                                <h4 style="padding-top: 8px;margin-top:10px">Isa green hand  </h4>
                                                                                                                                                            <h2 style="margin-top: 0px;padding-bottom: 26px"> Meet-and-greet </h2>h2</div>
                                                                                                                                                                    
                                                                                                                                                                            <span class="good-words" style="
                                                                                                                                                                                    position: absolute;
                                                                                                                                                                                            top: 98%;
                                                                                                                                                                                                    left: 10%;
                                                                                                                                                                                                            font-family: fantasy ;color:rgb(107, 167, 194)">
                                                                                                                                                                                                                        <h5 style="margin: 0px;">The quieter you become </h5>
                                                                                                                                                                                                                                    <h4 style="margin: 0px;"> The more you are able to hear </h4>h4</span>
                                                                                                                                                                                                                                            

                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                    <script src="static/jquery/dist/jquery.min.js"></script>
                                                                                                                                                                                                                                                        <script type="text/javascript" src="static/bootstrap/dist/js/bootstrap.js" ></script>
                                                                                                                                                                                                                                                        </body>
                                                                                                                                                                                                                                                        </html>

        """,

}
