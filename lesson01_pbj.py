Python-Lessons
==============

exercises for python class

bread = 15
jelly = 8
pb = 8

bread_needed = 2
jelly_needed = 1
pb_needed = 1

# ingredients check

if bread >=bread_needed and jelly >=jelly_needed and pb >=pb_needed:
	print "I can make a sandwich."
elif bread < bread_needed or jelly < jelly_needed or pb < pb_needed:
	print "I need to go to the grocery store."
	if bread < bread_needed:
		print "Buy bread."
	if jelly < jelly_needed:
		print "Buy jelly."
	if pb < pb_needed:
		print "Buy peanut butter."

# how many can I make
print "With my ingredients, I can make {0} sandwiches.".format(min(bread/bread_needed, jelly, pb))

# open faced sandwiches?

if bread%2 == 1 and jelly >= bread/2 + 1 and pb >= bread/2 + 1:
	print "Plus I get to treat myself to an open-faced sandwich."
