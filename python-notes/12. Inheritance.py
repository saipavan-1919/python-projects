"""
    Inheritance:
        Using the properties of one class in another class is known as inheritance.
        There are multiple level inheritances:
        1) single inheritance
        2) multi level inheritance
        3) multiple inheritance
        4) heirachical inheritance

        1) single inheritance:
            When a child class inherited properties from one parent class then it is known as single inheritance.
                  A(parent class) -> B(child class)
        2) multi level inheritance:
            When a parent class A is inherted into a child class B,
            and B is inherited into another child class
                  A(parent class) -> B(intermediate class) -> c(child class)
        3) multiple inheritance:
            If a class derived multiple parent classes then it is known as multiple inheritance.
                  A(parent class 1) -> C(child class)
                  B(parent class 2) -> C(child class)
        4) heirachical inheritance:
            when a parent class is inherited by multiple child classes then it is known as heirachical inheritance.
                  A(parent class) -> B(child class 1)
                  A(parent class) -> C(child class 2)
                  A(parent class) -> D(child class 3)
                  
"""

# single inheritance
# parent class
class A:
    def __init__(self):
        print("I'm a parent class")
    def fun(self):
        print("I'm from parent class")

#child class
class B(A):
    def __init__(self):
        print("I'm a child class")

obj = B()
obj.fun()


# multi level inheritance
# parent class
class A:
    def __init__(self):
        print("I'm a parent class")
    def fun_A(self):
        print("I'm from parent class")
# intermediate class
class B(A):
    def __init__(self):
        print("I'm a intermediate class")
    def fun_B(self):
        print("i'm from intermediate class")
# child class
class C(B):
    def __init__(self):
        print("I'm a child class")
    def fun_C(self):
        print("i'm from child class")

o = C()
o.fun_B()
o.fun_A()


# multiple inheritance
# parent class 1
class A:
    def __init__(self):
        print("I'm a parent class 1")
    def fun_A(self):
        print("I'm from parent class 1")
# parent class 2
class B:
    def __init__(self):
        print("I'm a parent class 2")
    def fun_B(self):
        print("I'm from parent class 2")
# child class
class C(A,B):
    def __init__(self):
        print("I'm child class")
    def fun_C(self):
        print("I'm from child class")


o1 = C()
o1.fun_A()
o1.fun_B()

# heirachical inheritance
# parent class
class A:
    def __init__(self):
        print("I'm a parent class")
    def fun_A(self):
        print("I'm from parent class")
# child class
class B(A):
    def __init__(self):
        print("I'm child class 1")
    def fun_C(self):
        print("I'm from child class 1")
# child class
class C(A):
    def __init__(self):
        print("I'm child class 2")
    def fun_C(self):
        print("I'm from child class 2")
# child class
class D(A):
    def __init__(self):
        print("I'm child class 3")
    def fun_C(self):
        print("I'm from child class 3")
