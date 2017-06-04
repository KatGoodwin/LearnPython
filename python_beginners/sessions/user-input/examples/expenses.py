input = ""
subtotal = 0

while True:
    input = raw_input("Please enter the amount spent: (Or 'quit' to exit)\n")
    if input.lower() == 'quit': break
    subtotal = subtotal + float(input)
    print "current subtotal: %.2f" %subtotal

print "Final total is: %.2f" %subtotal
