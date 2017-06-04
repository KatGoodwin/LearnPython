from Person import Person
class User(Person):
    def __init__(self, name, email):
       #super obtains the init from the base class.   
       super(User, self).__init__(name)
       self.email = email
        
    def greet(self):
        return "Hello, %s" % self.name # overriding parent's greet
    
    def send_email(self, message):
        return "emailing '%s' to %s" %(message, self.email)
   
if __name__ == "__main__":
    user = User("Barney", "Barney@rubble.com")
    print user.name
    print user.email
    print user.greet()
    print user.send_email("Hello")
    user.rebuke()
