import sys
import os

if os.path.exists("../src"):
    sys.path += ["../src"]
else :
    sys.path += ['/usr/local/lib/python2.7/site-packages/QTornado/src']
from init_filter import FillContentHandler

# load functional lib 
from lib import PathDecorator
from lib import XmlTag
import argparse

root_path= os.path.dirname(__file__)

fileSave = PathDecorator(root_path)

class TreeFile(FillContentHandler):

	def __init__(self,root,**kargs):
		self.root_path  = root
		self.static_path = os.path.join(self.root_path,"static")

		super(TreeFile, self).__init__()

	@fileSave.FileSave
	def initial_files(self,**options):
		cal_path = self.root_path

		def _path(fileName):
			return os.path.join(self.root_path,fileName)

		os.mkdir(_path("static"))
		os.mkdir(_path("template"))


		controller_file = _path("controller.py")
		controller_file_content = self.get_init_controller_file_content()

		setting_file = _path("setting.py")
		setting_file_content = self.get_init_setting_content()

		html_file =  _path( "template/index.html")
		html_file_content = self.get_html_content("index")

		main_file = _path("main.py")
		main_file_str = self.get_main_content()



		self._write_file(controller_file,controller_file_content)
		print "init  control \t ok"

		self._write_file(setting_file, setting_file_content)
		print "init  setting \t ok"

		self._write_file(html_file, html_file_content)
		print "init  html \t ok"

		self._write_file(main_file, main_file_str)
		print "run file load \t ok"

	def _write_file(self,file_name,content):
		with open(file_name,"w") as file_handler:
			file_handler.write(content)

	def add_content(self,file_name,content):
		with open(file_name,"a") as file_handler :
			print "\nadd controller ..."
			file_handler.write(content)

	@fileSave.FileSave
	def add_controller(self,name,**options):
		print "add controller : {}".format(name) ,
		cal_path = self.root_path

		path_name, handler_name =  self.get_path_handler_name(name)

		controller_file = os.path.join(cal_path,"controller.py")
		controller_file_content = self.get_new_controller(path_name)

		setting_file = os.path.join(cal_path,"setting.py")
		xmlTag = XmlTag(setting_file)
		xmlTag.changeTag("route", "(r'/{}',{}),".format(path_name,handler_name))

		viewname=path_name + ".html"
		template_dir = os.path.join(cal_path,"template")
		html_file = setting_file = os.path.join(template_dir , viewname)
		html_file_content = self.get_html_content(path_name)

		self.add_content(controller_file,controller_file_content)
		print "add success"
		self._write_file(html_file, html_file_content)

	def get_path_handler_name(self,string):
		return (string.lower() ,string[0].upper() + string[1:]+"Handler")


def handle_args():

	desc = """
this is a assistant for write web html
weite by Qingluan
github : http://github.com/Qingluan
	"""
	parser = argparse.ArgumentParser(usage='it is usage for qingluanTornado ', description=desc)
	parser.add_argument('pro_name_path',help="this argu is represent project's name")
	parser.add_argument('-i','--init',default=None)
	parser.add_argument('-c','--add-controller',default=None)
	parser.add_argument('-r','--re',default=False,type=bool)
	
	
	# args,remind = parser.parse_known_args(args)
	args = parser.parse_args()


	return args



			



if __name__ == "__main__":
	args = handle_args()

	fileSave.workpath =  os.path.join(root_path,args.pro_name_path)
	tree = TreeFile(args.pro_name_path)


	if args.init:
		if args.re:
			tree.initial_files(re=True)
		else:
			tree.initial_files()
		tree.add_controller(args.init)

	if args.add_controller:
		tree.add_controller(args.add_controller)

