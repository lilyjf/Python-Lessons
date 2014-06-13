bread = 12
jelly = 6
pb = 8
y = 1

bread_needed = 2
jelly_needed = 1
pb_needed = 1

while bread >= bread_needed and jelly >= jelly_needed and pb >= pb_needed:
	print "I'm making sandwich number {0}".format(y)
	bread = bread - 2
	jelly = jelly - 1
	pb = pb - 1
	y = y + 1
	print "I've got enough bread for {0} more sandwiches, enough jelly for {1}, and enough pb for {2}.".format(bread/2, jelly, pb)
	if bread < 2:
		print "\nTime to go to the store to buy more bread. I only had enough to make {0} sandwiches.".format(y-1)
	elif jelly <1:
		print "\nTime to go to the store to buy more jelly. I only had enough to make {0} sandwiches.".format(y-1)
	elif pb <1:
		print "\nTime to go to the store to buy more peanut butter. I only had enough to make {0} sandwiches.".format(y-1)

while bread >= 2 and jelly >= 1 and pb >= 1:
	print "I'm making sandwich number {0}".format(y)
	bread = bread - 2
	jelly = jelly - 1
	pb = pb - 1
	y = y + 1
	print "I've got enough bread for {0} more sandwiches, enough jelly for {1}, and enough pb for {2}.".format(bread * 2, jelly, pb)


