"""
    There are two types in sending arguments to a function
    1) pass by value:
        we send the arguments to the function to then the function will create the copy of those 
        arguments in its memory.
        if we do any changes then they won't reflect in the original values
        this type is used in cprogramming

    
    2) pass by refernce:
        We send the refernece to the arguments through a function 
        when we make any changes to the data in the function it will reflect in the original data.
        This is used in the python programming

    *** Python used call by refernece or pass by reference only 
"""
# pass by reference in python

def fun(arr):
    li.append(5)    

li = [1,2,3,4]
fun(li)
print(li)
