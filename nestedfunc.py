def parent(num):
	def child_one():
		return "This is child_one()function output"

	def child_two():
		return "This is child_two() output"

	try:
		assert num == 10
		return child_one()
	except AssertionError: 
		return child_two()

out1 = parent(10)
out2 = parent(11)

print("\tPrinting FUnctions Outputs")
print(out1)
print(out2)

#print("\tPrinting functions types")
#print(type(out1))
#print(type(out2))

print("\tPrinting functions defined")
print(parent(10))
print(parent(11))
