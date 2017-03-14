# define a function and its arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):

	# the number of cheese
	print "You have %d cheeses!" % cheese_count
	# the number of crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# print content
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# give a direct number of cheese and crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# use variable to give number of cheese and crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# do math to give number of cheese and crackers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# use variable and do math to give numbers of cheese and crackers
print "And we can combine the two, varaibles and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
