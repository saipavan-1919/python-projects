# iterator
"""
    Iterator is a object in python
    * iterator rememn=bers its state 
    * __iter__() method initializes the iterator object and returns a iterable object.
    * __next__() method is used to next values in the object when iterating/traversing through object.
        this method raise a StopIteration signal to stop the itertion of object.
    * list, strings, tuples are iterable object created using these methods.
    * we can see how they implemented from the following. 
"""

class iterable_class:
    # __init__ is constructor 
    # it initializes a object it runs automatically when we create a object
    # self is the instance of the class
    def __init__(self,li):
        self.li = li
    
    # __iter__ mehthod initializes iterable object and returns the iterable object.
    def __iter__(self):
        self.pos = 0
        return self
    
    # __next__ method will give the next element in the object
    def __next__(self):
        if self.pos < len(self.li):
            self.pos += 1
            return self.li[self.pos - 1]
        else:
            raise StopIteration

o = iterable_class([1,2,3,4])
for i in o:
    print(i)


