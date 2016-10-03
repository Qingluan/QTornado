import os
from Qtornado.initial_content import InitContent
from termcolor import colored
from Qtornado.log import LogControl

LogControl.LOG_LEVEL = LogControl.ERR

def default_input(String, default=''):
    val = input(String)
    if val:
        return val
    return default


class FillContentHandler(object):

    def __init__(self):
        self.content = InitContent
        import os
        self.static_res_path = os.path.join(os.getcwd(),"../resource/static")
        print( self.static_path)

    def get_init_controller_file_content(self):
        handler_str = self.content['BaseHandler']
        index_handler_str = self.content['handler']
        index_handler_str = index_handler_str %("Index","Index","index","")

        return "\n".join([handler_str,index_handler_str])

    def get_new_controller(self,name, websocket=False):
        # ensuer str 's first char is upper
        controller_name = name[0].upper() + name[1:]
        controller_name_low = name[0].lower() + name[1:]

        controller__str = self.content['handler'] if not websocket else self.content['websocket_handler']
        if websocket:
            controller__str = controller__str % (controller_name, controller_name, controller_name)
        else:
            controller__str = controller__str % (controller_name,controller_name,controller_name_low,controller_name_low)
        return controller__str

    def get_init_setting_content(self, type):
        setting_str = self.content['setting']
        con = ''

        database = default_input(colored('Choose a Database [local]\n:', 'cyan', attrs=['bold']), 
                default='local')
        con += 'database="%s",' % database

        if type == 'mongo':
            return setting_str % (database, "pymongo.Connection()['" + database + "']")

        
        sql_type = default_input(colored('sql type[sqlite] (mysql/postgresql) :', 'cyan', attrs=['bold']),
            default='sqlite')
        con += 'type="%s",' % sql_type

        if sql_type == 'sqlite':
            database = default_input(colored('Database file path [%s/db.sql]\n:' % os.getcwd() , 'cyan', attrs=['bold']),
            default="%s/db.sql" % os.getcwd())
            con = 'database="%s"' % database
            setting_str = setting_str % (con, "SqlEngine(%s)" % con)
            return setting_str

        host = default_input(colored('Host[127.0.0.1]:', 'cyan', attrs=['bold']), 
            default='127.0.0.1')
        con += 'host="%s",' % host

        user = default_input(colored('user[root]:', 'cyan', attrs=['bold']),
            default='root')
        con += 'user="%s",' % user

        passwd = default_input(colored('passwd[NULL]:', 'cyan', attrs=['bold']))
        con += 'password="%s"' % passwd

        
        if type == 'obj':
            setting_str = setting_str % (con, "SqlObjEngine(%s)" % con)
        else:
            setting_str = setting_str % (con, "SqlEngine(%s)" % con)

        return setting_str

    def get_model_content(self):
        setting_str = self.content['model_module']
        return setting_str

    def get_html_content(self, html_name, **options):
        left = 3
        right = 9
        try:
            if 'left' in options:
                left = int(options['left'])
            if 'right' in options:
                right = int(options['right'])
        except Exception as e:
            LogControl.err(e, left,right)
            raise(e)
            left = 3
            right = 9

        def _fill_args(string,*args):
            try:
                new_str = string % tuple( args)
                return new_str
            except TypeError:
                args = list(args) + [args[0]]
                new_args = tuple(args )
                return _fill_args(string,*new_args)
        if "theme" in options:
            if options['theme']:
                html_str = self.content[options["theme"]]
                try:
                    html_str = _fill_args(html_str,html_name)
                    return html_str
                except ValueError:
                    return html_str
        if "extends" in options:
            if options['extends']:
                html_str = self.content["extends_html"]
                try:
                    html_str = _fill_args(html_str,options['extends'])
                    html_str = html_str.replace(r'$', r'%')
                    return html_str
                except ValueError:
                    return html_str

        html_str = self.content['html']
        html_str = _fill_args(html_str ,html_name, html_name, left, left+1, right, right -1,  html_name, html_name)
        html_str = html_str.replace(r'$', r'%')
        return html_str

    def get_css_content(self, css_name):
        css_str = self.content['css']
        css_str = css_str % (css_name)
        return css_str

    def get_main_content(self):
        return self.content['main']

    def get_js_content(self,name,**options):
        js_str = self.content['js']
        js_str = js_str % (name)
        return js_str

    def get_ui_content(self):
        ui_template = self.content['ui_modules']
        return ui_template.replace(r'$', r'%')


if __name__ == '__main__':
    test = FillContentHandler()
    print( test.get_init_controller_file_content())
    print( test.get_init_setting_content())
    print( test.get_html_content("test"))
    
