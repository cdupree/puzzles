#!/usr/bin/env python

lockers = list()

def print_lockers(lockers):
	for i in range(1,101):
		if  lockers[i] == 1:
			print("{}:  {}".format(i, lockers[i]))

for i in range(0,101):
	lockers.append( 1 ) # open

for j in range(2,101):
	for i in range(1,101):
		if i % j == 0:
			lockers[i] ^= 1 # toggle (see notes below for other options)

print_lockers(lockers)

