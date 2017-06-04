# -*- coding: utf-8 -*-
# formatting numbers
# we need to have specified the coding, as we have a non-ASCII character
# (pound sign) somewhere in here

my_float = 98.2
my_int = 123

# to format numbers
print "My float is money so I want to format it like this: £%.02f" % my_float
print "We can format printed numbers using %4d and %5.2f and %s " % (10, 100.1234, 0.0002)

# we can use the format to do rounding:
print '%8.2f' % 9.667
print '%8.2f' % 9.333
