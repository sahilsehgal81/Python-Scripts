def func(var):
	return var + 1

print(func)

print(func(2))

print(type(func))

def func_with_func(func, arg):
	return func(arg)

print(func_with_func(func, 5))
