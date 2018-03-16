def my_decorator(some_function):

	def func1():
		print("Some function which is executin Before SOMEFUNC")
		some_function()
		print("Some func excutiong AFTER SOMEFUNC")
	return func1

def my_some_function():
	print("Now I got it!")

myfunc = my_decorator(my_some_function)

print(myfunc())
