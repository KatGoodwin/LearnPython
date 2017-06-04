#!/usr/bin/env python

mystring = "bob the dog"

# we can use if and in to see if a string contains a character
search = 'b'
if search in mystring:
    print "%r contains %r" %(mystring, 'b')
    
# or a set of characters in order
search = 'bob'
if search in mystring:
    print "%r contains %r" %(mystring, search)

# but not in a different order
search = 'teh'
if search in mystring:
    print "%r contains %r" %(mystring, search)   
else:
    print "%r does not contain %r" %(mystring, search)

# another way is to use the find() method
for search in ('teh', 'the'):
    idx = mystring.find(search)
    if idx == -1:
        print '%r does not contain %r' % (mystring, search)
    else:
        print '%r contains %r at index %i' % (mystring, search, idx)
