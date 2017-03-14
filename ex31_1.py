print "You enter a dark room with two doors. Do you go through door #1 or door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bears runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothspins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity tos your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You are in middle school class and taking an exam."
    print "1. You are taking math exam."
    print "2. You are taking english exam."
    
    Class = raw_input("> ")
    
    if Class == "2":
        print "You score 100 points. good job!"
    elif Class == "1":
        print "You score 50 points. Good job!"
    else:
        print "You escaped the exam, you are banned from school! Good job!"


else:
    print "You stumble around and fall on knife and die. Good job!"

