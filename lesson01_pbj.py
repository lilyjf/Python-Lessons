Python-Lessons
==============

exercises for python class

bread = 15
jelly = 6
pb = 8

bread_needed = 2
jelly_needed = 1
pb_needed = 1

# ingredients check
if bread >=bread_needed and jelly >=jelly_needed and pb >=pb_needed:
	print "I can make a sandwich."

# how many can I make
print "With my ingredients, I can make {0} peanut butter and jelly sandwiches." .format(min(bread/bread_needed, jelly, pb))

# open faced sandwiches?
if bread%2 == 1 and jelly >= bread/2 + 1 and pb >= bread/2 + 1:
	print "Plus I get to treat myself to an open-faced sandwich."

# what ingredients am I missing?
elif bread < bread_needed or jelly < jelly_needed or pb < pb_needed:
	print "I need to go to the grocery store and buy:"
	if bread < bread_needed:
		print "bread"
	if jelly < jelly_needed:
		print "jelly"
	if pb < pb_needed:
		print "peanut butter"

# no jelly
if bread >= bread_needed and pb >= pb_needed and jelly < 1:
	print "I can make a peanut butter sandwich but I need to rethink my priorities."

elif jelly >=1 and jelly < pb:
	print "With my ingredients, I can make {0} peanut butter and jelly sandwiches and {1} plain peanut butter sandwiches".format(min(bread/bread_needed, jelly, pb), (pb-jelly))
