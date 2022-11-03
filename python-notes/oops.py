"""
    OOPS concepts:
        1) class
        2) object
        3) Abstraction
        4) Encapsulation
        5) Inheritance
        6) Polymorphism
    class:
        class is a behavioural logical layout.
        A class can consist of mainly two things 
        1) data
        2) functions
        It is the blueprint which is followed by the objects.
    Object:
        The instance of a class is known as Object.
        Object is a physical entity.
        Object needs to be created to access the data.
    
    * self is a implicit instance 
    * List of arguments must start with a self.
    * Varibale which are declared inside a class and not in a function are known as Instance variables.

    Abstraction:
        Hiding the implementation details and showing essential details.

    Encapsulation:
        Binding data and function into a single entity.
        We know that classes consist of both data and functions.
        When a class consist of both data and functions is known as Encapsualtion.
        We can provide protection to the classes
        public     - any function or class can access 
        protected  - access for class and inherited class
        private    - access for only declared class
    Inheritance:
        Using the properties (data and functions) of one class in another class.
        We can inherit one class properties into another class.
        Derived class - child class (inherited)
        Base class    - parent class (declared)
    Polymorphism:
        Implementing different functionality with same name in a inherited class.
        We can write a function with same name in child class.

"""

# class creation
class my_class():
    id = 1
    def func1(self):
        print("hello world")

# object creation
obj1= my_class()

# accessing object elements
print(obj1.id)

# calling methods from a class
obj1.func1()

