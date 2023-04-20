import sys

if(len(sys.argv) == 3):
	try:
		A = int(sys.argv[1])
		B = int(sys.argv[2])
	except ValueError:
		print("AssertionError: only integers")
		exit()
	mysum = A + B
	print("Sum:", mysum)
	difference = A - B
	print("Difference:", difference)
	product = A * B
	print("Product:", product)
	try:
		quotient = A / B
		print("Quotient:", quotient)
	except:
		print("Quotient: ERROR (division by zero)")
	try:
		remainder = A % B
		print("Remainder:", remainder)
	except:
		print("Remainder: ERROR (modulo by zero)")
elif(len(sys.argv) != 1):
	print("AssertionError: Wrong number of arguments")
else:
	print("Usage: python operations.py <number1> <number2>")