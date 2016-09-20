InitContent = {
# this is setting file 's content 
    'setting':"""

## write by qingluan 
# this is a config file
# include db and debug , static path 
from os import path
# here to load all controllers
from log import LogControl
from QmongoHelper import Mongo
from controller import *

# db engine 
db_engine = Mongo('local')

# static path 
static_path = "./static"

# set log level
LogControl.LOG_LEVEL |= LogControl.OK
LogControl.LOG_LEVEL |= LogControl.INFO

Settings = {
        'db':db_engine,
        'L': LogControl
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

""",

# this is base handler for all handler to inherited
    'BaseHandler':"""
## this is write by qingluan 
# just a inti handler 
# and a tempalte offer to coder
import json
import tornado
import tornado.web
from tornado.websocket import WebSocketHandler


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


class SocketHandler(WebSocketHandler):
    \"\"\" Web socket \"\"\"
    clients = set()
    con = dict()
         
    @staticmethod
    def send_to_all(msg):
        for con in SocketHandler.clients:
            con.write_message(json.dumps(msg))
         
    @staticmethod
    def send_to_one(msg, id):
        SocketHandler.con[id(self)].write_message(msg)

    def json_reply(self, msg):
        self.write_message(json.dumps(msg))

    def open(self):
        SocketHandler.clients.add(self)
        SocketHandler.con[id(self)] = self
         
    def on_close(self):
        SocketHandler.clients.remove(self)
         
    def on_message(self, msg):
        SocketHandler.send_to_all(msg)

""",


# this is handler 's template

    'handler':"""


class %sHandler(BaseHandler):
    
    def prepare(self):
        super(%sHandler, self).prepare()
        self.template = "template/%s.html"

    def get(self):
        return self.render(self.template, post_page="/%s")

    @tornado.web.asynchronous
    def post(self):
        # you should get some argument from follow 
        post_args = self.get_argument("some_argument")
        # .....
        # for parse json post
        # post_args = json.loads(self.request.body.decode("utf8", "ignore"))['msg']
        
        # redirect or reply some content
        # self.redirect()  
        self.write("hello world")
        self.finish()
    """,
# this is json handler 's template
    'websocket_handler':"""


class %sHandler(SocketHandler):
    
    def open(self):
        super(%sHandler, self).open()
        self.json_reply({
            "type": "sys",
            "code": "true",
        })
        
         
    def on_close(self):
        super(%sHandler, self).on_close()
        
         
    def on_message(self, msg):
        # this is base function to write msg
        # self.write_message(msg) 

        # this is reply msg to all connection 
        # SocketHandler.send_to_all(msg)   

        # this is json ver to reply msg
        self.json_reply(msg)
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
    <h3>.. Qtornado ..</h3>
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
from setting import  appication, port

if __name__ == "__main__":
    appication.listen(port)
    tornado.ioloop.IOLoop.instance().start() 

    """,
#this is a ad for our ISC 

        'ISA':"""
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
