# variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

# print variables
print x
print y

# print string with format characters 
print "I said: %r." % x
print "I also said: '%s'." % y

# variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print string with format characters 
print joke_evaluation % hilarious

# variables
w = "This is the left side of ..."
e = "a string with a right side."

# print string
print w + e
