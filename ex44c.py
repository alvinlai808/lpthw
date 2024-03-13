class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()    # calls the parent class's function that has not been overridden by the subclass
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()   # overrides Parent.altered() because Child is a subclass
