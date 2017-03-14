#import a module 
#from sys import argv

#define the arguments
#script, filename = argv
filename = raw_input("Your filename is:")

#define txt function is to open a file
txt = open(filename)

# print file name and open the file
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# ask user to type in the filename again
print "Type the filename again:"
file_again = raw_input("> ")

#print file again with the filename given
txt_again = open(file_again)

print txt_again.read()
txt_again.close()
