"""
Functions in subclasses that share the same name with functions
in the base class will override the base function's functionality
and behave differently from the base function
"""

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()