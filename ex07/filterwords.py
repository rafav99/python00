import string
import sys

newlist= []
try:
	number = int(sys.argv[2])
	if len(sys.argv) == 3:
		mylist = sys.argv[1].split()
		for i in range(len(mylist)):
			mylist[i] = mylist[i].translate((str.maketrans('', '', string.punctuation)))
			if len(mylist[i]) > number:
				newlist.append(mylist[i])
		print(newlist)
	else:
		print("ERROR")
except:
	print("ERROR")
