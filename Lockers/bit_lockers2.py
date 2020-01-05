#!/usr/bin/python

lockers = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0x0000000F]

WORD_SIZE = 32

def print_lockers(lockers):
	for i in range(0,100):
		index = i / WORD_SIZE
		offset = i % WORD_SIZE
		if (lockers[index] & (1 << offset)):
			 print("Locker {} at index {} and offset {} is open".format(i + 1, index, offset))

for j in range(2, 101):
	for i in range(0, 100):
		if (i + 1 ) % j == 0:
			index = i / WORD_SIZE
			offset = i % WORD_SIZE
			lockers[index] ^= (1 << offset)

print_lockers(lockers)
