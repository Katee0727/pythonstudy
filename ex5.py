MyName = 'Zed A. Shaw'
MyAge = 35 # not a lie
MyHeight = 74 * 2.54 # cm
MyWeight = 180 * 0.453592 # kg
MyEyes = 'Blue'
MyTeeth = 'White'
MyHair = 'Brown'

print "Let's talk about %s." % MyName
print "He's %d centimeters tall." % MyHeight
print "He's %d kilograms heavy." % MyWeight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (MyEyes,MyHair)
print "His teeth are usually %s depending on the coffee." % MyTeeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( 
	MyAge, MyHeight, MyWeight, MyAge + MyHeight + MyWeight)

