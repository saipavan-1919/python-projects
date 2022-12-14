"""
    __str__ method:
        * __str__ method is a special type of method in the python class.
        * This method is used to show the all members of a class.
        * The __str__ method should be defined in a way that is easy to read and outputs all the members of the class. 
        This method is also used as a debugging tool when the members of a class need to be checked.
        * The __str__ method is called when the following functions are invoked on the object and return a string:
            1) print()
            2) str()
        * If we have not defined the __str__, then it will call the __repr__ method.
        * The __repr__ method returns a string that describes the pointer of the object by default (if the programmer does not define it).
"""

class sample:
    def __init__(self):
        print("a object of sample class is created")
    def __str__(self):
        print("i'm a __str__ method inside the sample class object")
        return "hi"


obj = sample()
print(obj)
str(obj)
