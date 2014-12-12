

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
		(r'/login',LoginHandler),
#<route></route>                # (r'/main',MainHandler),
         ],**Settings)


# setting port 
port = 8080

if __name__ == "__main__":
	appication.listen(8080)
	tornado.ioloop.IOLoop.instance().start() 

