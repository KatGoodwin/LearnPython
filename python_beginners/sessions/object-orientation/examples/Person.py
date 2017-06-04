class Person(object):
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return "Greetings, %s" % self.name

    def rebuke(self):
        print "%s, this is simply not acceptable" % self.name

if __name__ == '__main__':
    person = Person("Fred")
    print person.name
    print person.greet()
    person.rebuke()
