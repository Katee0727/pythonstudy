def add(a, b, c):
	print "I am going to add %d, %d and %d" % (a, b, c)
	return a + b + c

def subtract(a, b, c):
	print "Now is the subtraction: %d, %d and %d" % (a, b, c)
 	return a - b - c

age = add(10, 20 , 30)
weight = subtract(120, 10, 5)

print "My name is Kate, my age is: %d, my weight is: %d" % (age, weight)

print "I also have a puzzle"

puzzle = add(age, weight, 10)

print "The answer to the puzzle is: %d" % puzzle

