class MyStuff(object):

    # In the MyStuff function __init__ I then get this extra variable self,
    # which is that empty object Python made for me, and I can set variables 
    # on it just like you would with a module, dictionary, or other object.
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# initialize your newly created empty object which is then set with
# the 'tangerine' variable. i.e.: create an object from class MyStuff
# and assign that object to the 'thing' variable
thing = MyStuff() 
thing.apple() # get 'apple' from the object
print(thing.tangerine)

