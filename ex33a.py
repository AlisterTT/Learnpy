# -*- coding: utf-8 -*-
def loop(i):
	numbers = []
	while i < 13:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

i = input("> ") 
loop(i)