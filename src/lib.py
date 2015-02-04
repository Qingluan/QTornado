import os
import HTMLParser
import re
class PathDecorator(object):

	def __init__(self,path):
		self.workpath = path

	def FileSave(self,func):			
		def __file_work(*args,**kargs):
			kargs['path'] = self.workpath

			def _path(subfile):
				return os.path.join(self.workpath,subfile)

			if    "re" in kargs:
				print "re init project ...."
				try:
					os.rmdir(self.workpath)
				except OSError:
					files = os.listdir(self.workpath)
					print "remain incomplete files ... {} ".format(files)
					print "start clean it  "

					[ os.popen("rm  {} ".format(_path(file))) for file in files]

				print "rm old version "

			if not os.path.exists(self.workpath):
				print "mkdir root path"
				os.mkdir(self.workpath)				

			res =  func(*args,**kargs)
			return res
		return __file_work
		
class XmlTag(object):

	def __init__(self,file_name):
		self.file_name = file_name
		self.read_fp = open(self.file_name)

		

	def changeTag(self,tag,new):
		re_compile = re.compile(r'(\#<{}>)'.format(tag))
		print re_compile.pattern
		new_content = ""
                new = new[0].upper() + new.lower()[1:]
		for line in self.read_fp:
			if not re_compile.findall(line):

				new_content += line
			else :
				print "add  route : {} ".format(new[1:-1])
                                new_content += "\t\t{}\n#<{}></{}>\n".format(new,tag,tag[0].upper() + tag[1:] )

		self.read_fp.close()
		with open(self.file_name,'w') as fp:
			fp.write(new_content)
		
