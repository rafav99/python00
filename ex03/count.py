import string
import sys

def text_analyzer(text=None):
	'''This function counts the number of upper characters, 
lower characters, punctuation and spaces in a given text.'''
	if text is None:
		text = input("Insert text:\n")
	if not isinstance(text, str):
		print("AssertionError: argument is not a string")
	else:
		totalchars = len(text)
		upper = sum(1 for i in text if i.isupper())
		lower = sum(1 for i in text if i.islower())
		space = sum(1 for i in text if i == " ")
		punctuation = sum(1 for i in text if i in string.punctuation)
		print("The text contains", totalchars,"character(s)")
		print("-", upper, "upper letters(s)")
		print("-", lower, "lower letter(s)")
		print("-", punctuation, "punctuation mark(s)")
		print("-", space, "space(s)")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if len(sys.argv) == 2:
			text_analyzer(sys.argv[1])
		else:
			print("Error: more than one argument are provided")
