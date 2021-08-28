def get_text(name):
	name = 'bro'
	print('get_text')
	return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
	print('p_decorate')
	def func_wrapper(name):
		print('func_wrapper')
		print(func, name)
		return "<p>{0}</p>".format(func(name))
	return func_wrapper

my_get_text = p_decorate(get_text)

print(my_get_text("John"))
