#!/usr/bin/python
from operator import itemgetter
import sys

requests = 0
data = 0.0
costs = 0.0

# input from STDIN
for request in sys.stdin:

	request = request.strip() # remove leading and trailing whitespace
	machine, byte = request.split('\t', 1) # parse the input we got from mapper

    # convert byte (currently a string) to int
	try:
		byte = int(byte)
	except ValueError:
		continue # byte was not a number, so silently ignore/discard this line
	
	# calculate total number of requests and volume of data
	requests = requests+1
	data = data+byte

# format data
# 2**10 = 1024
power = 2**10
n = 0
data_labels = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
while data > power:
	data /= power
	n += 1

#calculate costs
costs = 0.001*requests + data*(0.08*(1024**(n-3)))

# write results to STDOUT
print 'Total number of requests:\t%s' % (requests)
print 'Total volume of transferred data:\t%f %s' % (data, data_labels[n])
print 'Total CDN billing costs (rounded to 2 decimals):\t%s cents' % (round(costs,2))
