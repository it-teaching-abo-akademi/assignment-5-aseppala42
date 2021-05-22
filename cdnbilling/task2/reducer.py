#!/usr/bin/python
from operator import itemgetter
import sys
import socket

domains = {}

# input from STDIN
for request in sys.stdin:

	request = request.strip() # remove leading and trailing whitespace
	machine, byte = request.split('\t', 1) # parse the input we got from mapper

    # check if machine is an ip address
	try:
		socket.inet_aton(machine)
		continue
	except:
		pass # machine was not an ip address

	# check if domain is valid
	try:
		machine = machine.split('.')
		domain = machine[-2]+'.'+machine[-1]
	except:
		continue # domain was not valid, so silently ignore/discard this line
	
	try:
		domains[domain] = domains[domain]+1
	except:
		domains[domain] = 1

# sort words
sorted_domains = sorted(domains.items(), reverse=True, key=lambda item: item[1])

# write max 5 most popular domains to standard output STDOUT
for domaincount in sorted_domains[:5]:
	print '%s\t%s' % (domaincount[0], domaincount[1])
