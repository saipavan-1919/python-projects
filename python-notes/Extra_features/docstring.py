# doc string
"""
    Doc string:
        Doc string is a string used in the functions, classes, methods
        to tell the what that function will do

        * Docstring explains about the function/class funcitonality.
        * it should explain what it do's not how it do.

        we have __doc__ variable to know the docstring of a function 

"""

def fun():
    """This function will print hi
    """
    print("hi")

print(fun.__doc__)

# help will print the docstring
help(fun)
