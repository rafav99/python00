import sys

if len(sys.argv) > 1:
	allarg = " ".join(sys.argv[1:])
	rev_str = allarg[::-1]
	final_str = rev_str.swapcase()
	print(final_str)