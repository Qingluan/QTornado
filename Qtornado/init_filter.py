from Qtornado.initial_content import InitContent

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

    def get_init_setting_content(self):
        setting_str = self.content['setting']
        return setting_str


    def get_html_content(self,html_name,**options):
        def _fill_args(string,*args):
            try:

                new_str = string % tuple( args)
                return new_str
            except TypeError:
                args = list(args) + [args[0]]
                new_args = tuple(args )
                return _fill_args(string,*new_args)
        if "theme" in options:
            html_str = self.content[options["theme"]]
            try:
                html_str = _fill_args(html_str,html_name)
                return html_str
            except ValueError:
                return html_str
        if "extends" in options:
            html_str = self.content["extends_html"]
            try:
                html_str = _fill_args(html_str,options['extends'])
                html_str = html_str.replace(r'$', r'%')
                return html_str
            except ValueError:
                return html_str

        html_str = self.content['html']
        html_str = _fill_args(html_str ,html_name)
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


if __name__ == '__main__':
    test = FillContentHandler()
    print( test.get_init_controller_file_content())
    print( test.get_init_setting_content())
    print( test.get_html_content("test"))
    
