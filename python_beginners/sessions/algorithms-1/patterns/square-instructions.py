starts = (2,4,6,8,10,12,14)

print "<html><head></head><body>"
print "<h1>Instructions for generating <img src='multiple-squares.png'>"
print "<ul>"

for start in starts:
    
    length = 30 - (start *2)
    print "<li>set(%s,%s)</li>" %(start, start)
    print "<li>move(%s)</li>" %length
    for num in range(3):
        print "<li>turn(left)</li>"
        print "<li>move(%s)</li>" %length
    

print "</ul>"

