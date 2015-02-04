#!/usr/bin/python

import sys
import os



src_path = '/usr/local/lib/python2.7/site-packages/QTornado/src'
resource_path = '/usr/local/lib/python2.7/site-packages/QTornado/resource/static'

if not os.path.exists(src_path) : 
    print "not installed  completed ... yet or version isn't match"
    src_path = "./" 
    resource_path = "../resource/static"


sys.path += [src_path]

# load functional lib 

from init_filter import FillContentHandler
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
        
        if not os.path.exists(self.root_path):
            os.mkdir(self.root_path)
        
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

        print "manifest file copy is\t",
        os.popen("cp {}  {}".format(os.path.join( src_path,"manifest.py"), cal_path))
        print "  ok"

        print "init  control \t",
        self._write_file(controller_file,controller_file_content)
        print " ok"

        print "init setting ",
        self._write_file(setting_file, setting_file_content)
        print "\t ok"

        print "init html ",
        self._write_file(html_file, html_file_content)
        print "\t ok"

        print "run file load ",
        self._write_file(main_file, main_file_str)
        print "\t ok"

        print "static res build ...",
        com = "cp -a {}/*  {}".format(resource_path,_path("static"))
        os.popen(com)
        print "ok in  "

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
        handler_name = handler_name[0].upper() + handler_name[1:]
        print handler_name
        xmlTag.changeTag("route", "(r'/{}',{}),".format(path_name,handler_name[0].upper() + handler_name[1:] ))

        viewname=path_name + ".html"
        template_dir = os.path.join(cal_path,"template")
        html_file  = os.path.join(template_dir , viewname)
        html_file_content = self.get_html_content(path_name,**options)

        css_name = name.lower()
        css_dir = os.path.join(self.static_path,"css")
        css_file = os.path.join(css_dir ,css_name+ ".css")
        css_content = self.get_css_content(css_name)
        self._write_file(css_file,css_content)

        js_name = name.lower()
        js_dir = os.path.join(self.static_path,"js")
        js_file = os.path.join(js_dir,js_name + ".js")
        js_content = self.get_js_content(js_name)
        self._write_file(js_file, js_content)

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
    parser.add_argument('-p','--pro_name_path',help="this argu is represent project's name")
    parser.add_argument('-i','--init',default=None)
    parser.add_argument('-c','--add-controller',default=None)
    parser.add_argument('-r','--re',default=False,type=bool)
    parser.add_argument('-t','--theme-choice',default=None) 
    parser.add_argument('-u','--uninstall',action="store_true",default=False)
    parser.add_argument('-e','--extends',default=None,help="this is for add  a new   template that will  extend another template \n example : -e main")

    # args,remind = parser.parse_known_args(args)
    args = parser.parse_args()


    return args



            



if __name__ == "__main__":
    args = handle_args()
    
    if args.pro_name_path:
        if "/" in args.pro_name_path:
            fileSave.workpath =  os.path.join(root_path,args.pro_name_path)
            tree = TreeFile(args.pro_name_path)
        else :
            fileSave.workpath = "./"
            tree = TreeFile(args.pro_name_path)

    if args.init:
        if args.re:
            tree.initial_files(re=True)
        else:
            tree.initial_files()
        tree.add_controller(args.init)

    if args.add_controller:
        if args.theme_choice:
            tree.add_controller(args.add_controller,theme=args.theme_choice)
        elif args.extends:
            tree,add_controller(args.add_controller,extends=args.extends)
        else:
            tree.add_controller(args.add_controller)
    if args.uninstall :
        if os.path.exists('/usr/local/bin/Qtornado.py'):
            os.popen("rm /usr/local/bin/Qtornado.py*").read()
        if os.path.exists('/usr/local/lib/python2.7/site-packages/QTornado'):
            os.popen("rm -rf /usr/local/lib/python2.7/site-packages/QTornado")

