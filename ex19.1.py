def kate_function(arg1, arg2):
	print "Kate will cook: %r for lunch today" % arg1
	print "Steve will cook: %r for dinner today" % arg2
	print "Wow, we have yummy food to eat, no need to eat outside"
	print "We should keep doing this!"

# use variables to use function
arg1 = "Chinese food"
arg2 = "Pasta"

kate_function(arg1, arg2)

# use format characters and users' input to use function
prompt = '>'

print "What do you want eat for lunch"
arg1_new = raw_input(prompt)

print "What do you want eat for dinner"
arg2_new = raw_input(prompt)

kate_function(arg1_new, arg2_new)


