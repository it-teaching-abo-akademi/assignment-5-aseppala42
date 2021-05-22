#!/usr/bin/python
import sys
# input from standard input STDIN
for request in sys.stdin:
	request = request.strip() # remove leading and trailing whitespaces
	fields = request.split() # split the request into fields and returns as a list
	# write the results to standard output STDOUT
	print'%s\t%s' % (fields[0],fields[-1])
