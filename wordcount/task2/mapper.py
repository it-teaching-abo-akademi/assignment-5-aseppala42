#!/usr/bin/python
import sys

words = {}

# input from standard input STDIN
for line in sys.stdin:

	line = line.strip() # remove leading and trailing whitespaces
	tmp = line.split() # split the line into words and returns as a list

	# combiner reduces the local intermediate pairs 
	for word in tmp:
		try:
			words[word] = words[word]+1
		except:
			words[word] = 1

for word, count in words.items():
	# write the results to standard output STDOUT
	print'%s\t%s' % (word,count)
