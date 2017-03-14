numbers = []

def count(i , x):

    while i <= x:
        print "At the top i is %d" % i
        numbers.append(i)

        i += i
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers:"

    for num in numbers:
        print num

#name = count(0, 6)

#print "convert to function: %r" % name

def clear():
    while len(numbers) >= 1:
        numbers.pop()    
