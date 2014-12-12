from initial_content import InitContent

class FillContentHandler(object):

	def __init__(self):
		self.content = InitContent

	def get_init_controller_file_content(self):
		handler_str = self.content['BaseHandler']
		index_handler_str = self.content['handler']
		index_handler_str = index_handler_str %("Index","Index","Index","Index")

		return "\n".join([handler_str,index_handler_str])

	def get_new_controller(self,name):
		# ensuer str 's first char is upper
		controller_name = name[0].upper() + name[1:]
		controller__str = self.content['handler']
		controller__str = controller__str % (controller_name,controller_name,controller_name,controller_name)
		return controller__str

	def get_init_setting_content(self):
		setting_str = self.content['setting']
		return setting_str


	def get_html_content(self,html_name):
		html_str = self.content['html']
		html_str = html_str % (html_name,html_name)
		return html_str

	def get_main_content(self):
		return self.content['main']


if __name__ == '__main__':
	test = FillContentHandler()
	print test.get_init_controller_file_content()
	print test.get_init_setting_content()
	print test.get_html_content("test")
	