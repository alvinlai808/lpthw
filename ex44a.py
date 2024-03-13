"""
Functions in a base class (the Parent) will automatically be shared
with all subclasses (the Child/any children)
"""

class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()