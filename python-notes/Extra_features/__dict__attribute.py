"""
    __dict__ attribute:
        * The __dict__ attribute is used to make all the varibles in the objects as a dictionary.
        * All the objects have a attribute called as __dict__
        * This will convert all the variables into the dictionary.
        * __dict__ will create dictionary with class instances (which are declared as self.<var_name> only)
        * which are self.varaibles they only gets converted as the dictionary
"""



class sample:
    n1 = "how"                  # it will be not included in the dictionary
    def __init__(self):
        self.fname = "sai"
        self.sname = "pavan"
        self.tname = "kumar"
        initial = "nibhanupudi"  # it will be not included in the dictionary
    def pri(self):
        self.name = "hi"
        print(self.fname)
        print(self.__dict__)
    
obj = sample()
print(obj.__dict__)  # here it will not include the slef.name because it is not defined at this point
obj.pri()            # here we are initializing self.name 
print(obj.__dict__)  # in this dictionary "name" also gets included

# vars is method which will generate the dictionary of variables from a object
print(vars(obj))
