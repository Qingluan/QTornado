
#!/usr/bin/python
## write by qingluan 
# just a run file 

import tornado.ioloop
from tornado.ioloop import IOLoop
from setting import  appication

if __name__ == "__main__":
	appication.listen(8080)
	tornado.ioloop.IOLoop.instance().start() 

	