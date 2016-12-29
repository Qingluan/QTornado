InitContent = {
# this is setting file 's content 
    'setting':"""

## write by qingluan 
# this is a config file
# include db and debug , static path 
import os
from os import path
# here to load all controllers
from Qtornado.log import LogControl
from Qtornado.db import *
from controller import *

# load ui modules
import ui
import sys

# db engine 
# db_engine = pymongo.Connection()['local']
db_connect_cmd = r'%s'
db_engine = %s


# static path 
rdir_path = os.path.dirname(__file__)
static_path = rdir_path + r"\static" if sys.platform.startswith("win") else "./static"
files_path = rdir_path + r".\static\\files" if sys.platform.startswith("win") else "./static/files"
# set log level
LogControl.LOG_LEVEL |= LogControl.OK
LogControl.LOG_LEVEL |= LogControl.INFO

Settings = {
        'db':db_engine,
        'L': LogControl,
        'debug':True,
        "ui_modules": ui,
        'autoreload':True,
        'cookie_secret':'This string can be any thing you want',
        'static_path' : static_path,
    }


## follow is router
try:
    os.mkdir(files_path)
except FileExistsError:
    pass
#
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
        self.L = self.settings['L']
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
        # L is log function , which include ok , info , err , fail, wrn
        self.L.ok('got')
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>%s</title>     
    <link href="/static/bootstrap/dist/css/bootstrap.css" rel="stylesheet"></link>
    {$ block head_css $}
         <link href="/static/css/%s.css" rel="stylesheet"></link>
    {$ end $}
    
    {$ block extends_css $}
    {$ end $}
</head>     
<body>      
    <div class="main" class='main'>
        <div class="body">
            {$ block left_d $}
            <div class="left col-md-%d col-sm-%d col-xs-12">
            {$ module Nav([
            {
                'txt':'Index',
                'link': '/',
                'active': '1',
                'tq': '1'
            },
            {
                'txt':'Sql Inject',
                'link': '/sqlinject',

            },] ,title='Index') $}
            {$ block left $}
            {$ end $}
            {$ end $}
                
            </div>

            {$ block content_d $}
            <div class="content col-md-%d col-sm-%d col-xs-9">
                <div class="head">
                {$ block head $}
                    <h1>Hacker Sites <small>ok?</small></h1>
                    <p>%s</p>
                    {$ module Files() $}
                {$ end $}
                </div>
            {$ block content $}
                <p>test</p>
                
            {$ end $}
            </div>
            {$ end $}
        </div>
        <div class="tail">
        {$ block tail $}
        {$ end $}
        </div>
    </div>
    

    <script src="/static/jquery/dist/jquery.min.js"></script>
    <script src="/static/bootstrap/dist/js/bootstrap.js"></script>
    {$ block body_js $}
        <script src="/static/js/%s.js"></script>
        <!--
        <script type="text/javascript">
            websocket = new web_client("ws://localhost:8080/[url]")
            websocket.on_msg(function(json){
                console.log(json);
            }
        </script> 
        -->
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
    <!--
    <script type="text/javascript">
        websocket = new web_client("ws://localhost:8080/[url]")
        websocket.on_msg(function(json){
            console.log(json);
        }
    </script> 
    -->
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


def main():
    appication.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
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
        'model_module':"""
# this is just template , will be parse to 
# written by Qingluan 
# CREATE TABLE task (
#        ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT ,
#        CreatedTime TimeStamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#        task_name varchar(255) not null default "default_task",
#        status varchar(255) not null default "status",
#        url TEXT)
#
#
#
class tables:
    taks = {'task_name': 'default_task', 'url': str, 'status': 'status'}

""",
        'ui_modules': """
import tornado.web
import os

class Card(tornado.web.UIModule):
    
    def render(self, title, img_url='images/hat.png', content='...', html=None):
        return self.render_string('template/ui_templates/card.html', 
            title=title, 
            img_url=img_url,
            html=html,
            content=content,
        )

    
    def embedded_css(self):
        return '''
            .card-container {
                background: #ebebeb;
                margin:10px;
                border-radius: 25px; 
            }

            .card-container > .card {
                background: #fafafa;
                border: 2px solid white;
                border-radius: 20px;
                margin: 2px;
            }

            .card > img {
                width: 60px;
                height: 60px;
                float: left;
                margin-right: 30px;
                margin-bottom: 30px;
                padding: 4px;
                border: 2px solid #fff;
                background: rgb(229, 229, 229);

            }
        '''


class Inputs(tornado.web.UIModule):
    \"\"\"
    type: horizontal/ inline . this will be parse to form-horizontal/ form-inline in bootstrap
    \"\"\"

    types = (
        'text',
        'file',
        'email',
        'submit',
        'button',
        'checkbox',
        'password',
    )

    def classify(self, name):
        res = name.split(":")
        if len(res) == 2:
            tpe, name = res
            if tpe not in Inputs.types:
                name, v = res
                return ['text', name, v]
            else:
                return [tpe, name, '']
        elif len(res) == 3:
            tpe, name, value = res
            if tpe not in Inputs.types:
                raise Exception("not found input type $s" $ tpe)
            return [tpe, name, value]
        elif len(res) == 1:
            return ['text', res[0], '']


    def render(self, *inputs, type='normal', title=None, form_type='horizontal', action='#', method='post'):
        inputs = [ self.classify(input) for input in inputs ]
        return self.render_string('template/ui_templates/{t}_inputs.html'.format(t=type), 
            inputs=inputs,
            type=form_type,
            title=title,
            action=action,
            method=method,
        )


    # def html_body(self):
    #     return '<script>document.write("Hello!")</script>'


class Table(tornado.web.UIModule):

    def rows(self, head_num, items):
        body = [[items[ii*head_num + i] for i in range(head_num)] for ii in range(int(len(items) / head_num ))]
        if len(items) $ head_num != 0:
            yu = len(items) $ head_num
            all_len = len(items)
            return body + [[items[i] for i in range(all_len - yu, all_len)]]
        return body


    def render(self,table_headers , *table_items, type='normal', title='', table_type='striped'):
        items = self.rows(len(table_headers), table_items)
        return self.render_string('template/ui_templates/{t}_table.html'.format(t=type), 
            headers=table_headers,
            items=items,
            type=table_type,
            title=title,
        )



class Nav(tornado.web.UIModule):
    \"\"\"
    items example:
        [{
            'txt':'xxx',
            'link': '/index',
            'active': '1',
            'tq': '1'
        },
        {
            'txt':'xxx',
            'link': '/url',

        },
        {
            'txt':'xxx',
            'link': '/index2',
        }]
    \"\"\"

    def render(self, items, type='normal', title='Dashboard', nav_type='stacked'):
        return self.render_string('template/ui_templates/{t}_nav.html'.format(t=type), 
            items=items,
            type=nav_type,
            title=title,
        )

    def embedded_css(self):
        return '''
.tq{
    padding-left: 15px;
    padding-right: 15px;
    margin-bottom: 5px;
    font-size: 85%;
    font-weight: 100;
    letter-spacing: 1px;
    color: #51586a;
    text-transform: uppercase;
    
}

.nav > li > a{
    position: relative;
    display: block;
    padding: 7px 15px 7px ;
    padding-left: 27px;
    border-radius: 4px;
}

.nav > li.active > a {
    color: #252830;
    background-color: #e5e5e5;
}
li.divider{
    width: 70%;
    align-self: center;
    align-content: center;
    left:10%; 
    height: 1px;
    margin: 9px 1px;*
    margin: -5px 0 5px;
    overflow: hidden;
    bottom:10px;
    background-color: #e5e5e5;
    border-bottom: 1px solid #e5e5e5;    
}
        '''

class Files(Nav):
    \"\"\"
    items example:
        Files(file_path)
    \"\"\"
    def get_len(self, f):
        l = os.stat("./static/files/" + f).st_size
        s = "%f B" % float(l)
        if l / 1024 > 1:
            s = "%2.2f KB" % float(l/ 1024)
        else:
            return s

        if l / 1024 ** 2 > 1:
            s = "%2.2f MB" % float(l/ 1024 **2)
        else:
            return s

        if l / 1024 ** 3 > 1:
            s = "%2.2f GB" % float(l/ 1024 **3)
        else:
            return s

    def render(self, type='normal', title='Dashboard', nav_type='stacked'):
        ss = [{
            "txt":f,
            "link":"/static/files/" + f,
            "code": f.split(".").pop() + "[%s]" % self.get_len(f)
        } for f in os.listdir("./static/files")]
        return super().render(ss, type=type, title=title, nav_type=nav_type)

        """,

}
