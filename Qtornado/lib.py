from Qtornado.log import LogControl
import os
import re

LogControl.LOG_LEVEL |= LogControl.INFO

class PathDecorator(object):

    def __init__(self,path):
        self.workpath = path

    def FileSave(self,func):            
        def __file_work(*args,**kargs):
            kargs['path'] = self.workpath

            def _path(subfile):
                return os.path.join(self.workpath,subfile)

            if  "re" in kargs:
                LogControl.info("re init project ....")
                try:
                    os.rmdir(self.workpath)
                except OSError:
                    files = os.listdir(self.workpath)
                    LogControl.info("remain incomplete files ... {} ".format(files))


                    [ os.popen("rm  {} ".format(_path(file))) for file in files]

                LogControl.info("rm old version ")

            if not os.path.exists(self.workpath):
                LogControl.info("mkdir root path")
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
        LogControl.info(re_compile.pattern)
        new_content = ""
        for line in self.read_fp:
            if not re_compile.findall(line):
                new_content += line
            else :
                LogControl.info("add  route : {} ".format(new[1:-1]))
                new_content += "\t\t{}\n#<{}></{}>\n".format(new,tag,tag )

        self.read_fp.close()
        with open(self.file_name,'w') as fp:
            fp.write(new_content)
        
