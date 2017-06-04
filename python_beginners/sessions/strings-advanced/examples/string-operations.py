#!/usr/bin/env python

s = "this is a string"
print "the string is %d characters long." % len(s)

# replacing elements
s = s.replace ("a", "the")
print s

# splitting strings
bits = s.split() #by default splits on spaces
print type(bits)
print "%r" % bits

s = s.replace(" ", ",")
bits = s.split(",")
print "%r" %bits

s = s.upper()
print "String (UC) %s" % s

s = s.lower()
print "String (LC) %s" % s

# there are also isupper() or islower()
