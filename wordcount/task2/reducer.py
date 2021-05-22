#!/usr/bin/python
from operator import itemgetter
import sys

words = {}

# input from STDIN
for line in sys.stdin:

	line = line.strip() # remove leading and trailing whitespace
	word, count = line.split('\t', 1) # parse the input we got from mapper

    # convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		continue # count was not a number, so silently ignore/discard this line

	try:
		words[word] = words[word]+count
	except:
		words[word] = count

# sort words
sorted_words = sorted(words.items(), reverse=True, key=lambda item: item[1])

# write max 100 most frequent words to standard output STDOUT
for wordcount in sorted_words[:100]:
	print '%s\t%s' % (wordcount[0],wordcount[1])
