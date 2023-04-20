import sys

if(len(sys.argv) > 1):
	try:
		my_int = int(sys.argv[1])
		if(len(sys.argv) == 2):
			if(my_int == 0):
				print("I'm Zero.")
			elif(my_int % 2 == 1):
				print("I'm Odd.")
			else:
				print("I'm Even.")
		else:
			print("AssertionError: more than one argument are provided")
	except:
		print("AssertionError: argument is not an integer")
