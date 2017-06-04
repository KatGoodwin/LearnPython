#create tuple
record = ('Clockwork Software', 'Birmingham', 'www.clocksoft.co.uk')

#auto unpack
name, location, web = record

#auto pack
name2 = 'Penguisoft'
location2 = 'North Pole'
web2 = 'www.penguisoft.com'
new_record = name2, location2, web2
print new_record

# these are all equivalent
print "name=" + name + ", location=" + location + ", web=" + web
print "name=%s, location=%s, web=%s" % (name, location, web)
print "name=%s, location=%s, web=%s" % record

print "record = %s" % record # Won't work! expects 3 placeholders, just like previous example
print "record = %s" % (record,) #force it to be treated as a single element when unpacked
