import time

def time_checker(some_function):
	"""This is some function
          which would define decorators
          in nutshell"""

	def test_func():
		t1 = time.time()
		some_function()
		t2 = time.time()
		return "The difference between the functions would be " + str((t2 - t1)) + "\n"
	return test_func

@time_checker
def new_func():
	numlist = []
	for num in range(0, 10000000):
		numlist.append(num)
	print("\nSum Output would be like " + str(sum(numlist)))

print(new_func())
