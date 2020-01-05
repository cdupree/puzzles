#!/usr/bin/env python

lockers = 0xFFFFFFFFFFFFFFFFFFFFFFFFF

def print_lockers(lockers):
	for i in range(1,101):
		if lockers & (1 << i - 1):
			print("locker {} is open".format(i))

for j in range(2, 101):
	for i in range(1, 101):
		if i % j == 0:
			lockers ^= (1 <<  i - 1 )

print_lockers(lockers)
