from sys import argv

script, filename = argv

print "Now I will try to read the file %r i just created" % filename

txt = open(filename)

print txt.read()
txt.close()
