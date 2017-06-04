class MyFirstClass(object): 
    def __init__(self, text):
        self.text = text
        print "__init__ called with text " + text
        
    def print_text(self):
        print "lets do something with our text:"
        for char in self.text:
            print char

ob = MyFirstClass("hello")
ob.print_text()
