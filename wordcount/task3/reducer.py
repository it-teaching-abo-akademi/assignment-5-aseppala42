#!/usr/bin/python
from operator import itemgetter
import sys

three = 0
five = 0

# input from STDIN
for line in sys.stdin:

	line = line.strip() # remove leading and trailing whitespace
	word, count = line.split('\t', 1) # parse the input we got from mapper

    # convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		continue # count was not a number, so silently ignore/discard this line

	if (len(word) == 3):
		three = three+count
	elif (len(word) == 5):
		five = five+count

# write result to STDOUT
print 'Found %s 3-char length words.' % (three)
print 'Found %s 5-char length words.' % (five)

