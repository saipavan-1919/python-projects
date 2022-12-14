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
print(obj.__repr__())



# Case 1
# NO __str__ and NO __repr__ method defined
# Then the output of both __str__ and __repr__ will be same
class sample1:
    def __init__(self):
        print("sample1 object")

obj1 = sample1()
print(obj)  # this will call the __repr__ method 
print(obj1.__repr__())
print(obj1.__str__())


# Case 2
# Define __str__ method and NO __repr__ method
# Then the when we call the object in print it will call __str__
class sample2:
    def __init__(self):
        print("sample2 object")
    def __str__(self):
        return "i'm the sample2's __str__"

obj2 = sample2()
print(obj2) # this will call the __str__ method
print(obj2.__str__())
print(obj2.__repr__())


# case 3
# Defining __repr__ and __str__ methods
# Then the object will call __str__ method
class sample3:
    def __init__(self):
        print("sample3 object")
    def __str__(self):
        return "sample3 __str__ method"
    def __repr__(self):
        return "sample3 __repr__ method"
   

obj3 = sample3()
print(obj3) # this will call __str__ method
print(obj3.__repr__())
print(obj3.__str__())
