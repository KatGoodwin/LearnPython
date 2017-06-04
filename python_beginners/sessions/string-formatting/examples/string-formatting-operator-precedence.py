# % is a used for string formatting    
print "The result of 3 * 4 + 2 is %d" %  (3 * 4 + 2)

extn = 'TXT'
# Precedence can have unintended effects ...
print 'Your file, "%s", cannot be found' % "README."+extn

# Or cause an error
print "The result of 3 * 4 + 2 is %d" %  3 * 4 + 2
