"""
    Decorators:
        Decorators are functions in python that takes another function as a
        argument and extends the behaviour without explixitly modifying it.
        * A decorator takes a function as argument and adds some functionality to it
        * we use @ symbol to indicate that is a decorator.
        ex: 
            def decorator_fun(func):
                def inner():
                    print("hello")
                return inner
            @decorator_fun
            def func1():
                print("hi")
            func1()
        * In the above example decorator_fun is decorator function for the func1.
        * When we call func1() the decorator_fun() gets executed with func1 as the argument.
        * The inner function in a function is known as the closure function.
        * Closure function remembers the variables of outer function if the outer is already executed also.

"""


# In python everyhting is a object 
# function is also a object so we can store function name as a object.
def func1():
    print("hello ")

fun_var = func1
fun_var()


# passing function as argument
def func1(func): # taking function as argument
    print("Before execuiting func")
    func()
    print("after executing func")
def func2():
    print("this is func2")
func1(func2)  # passing function as argument

# decorator
def func1(func):
    def inner():
        print("i'm a decorator")
        func()
    return inner

def func2():
    print("i'm the original function")

dec_fun = func1(func2)  # these two steps can be eliminated with @ inclusion
dec_fun()

# we can modify the above decorator using @ symbol
# 
def func1(func):
    def inner():
        print("i'm decorator")
        func()
    return inner
@func1
def func2():
    print("i'm the original func")
# when we call the func2 then func1 will get executed with func1 as argument
func2()
