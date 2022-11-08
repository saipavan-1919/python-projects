"""
    Access specifiers:
        There are  three types of access specifiers in python.
        1) public
        2) protected
        3) private

        1) public members:
            These members can be accessed entire the program.
        2) protected members:
            These members can only be accessed in the derived and base class.
            These members need to be defined with a prefix '_'
        3) private members:
            These can only be accessed inside the class cannot access outside.
            These members need to be defined using '__'
"""

class class1:
    def __init__(self):
        self.n1 = "hi"     # public member
        self._n2 = "how"   # protected member
        self.__n3 = "are"  # private member
    
    def meth(self):
        print(self.__n3,self._n2,self.n1)

ob = class1()
ob.meth()
print(ob.n1)
print(ob._n2)
#print(ob.__n3) cannot be performed 
