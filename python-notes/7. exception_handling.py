"""
    Exception Handling:
        In python there are two types of errors/exceptions. they are
        1) syntax errors
        2) programming errors

        * syntax errors can be solved by changing the wrong syntax into the correct one.
        * Programming errors cannot be solved they raises exceptions.
            To handle those exceptions in python we have exception handling statements.
            they are  
            a) try block        - it will executed first or tried first (we can have exeptions here)
            b) except block     - if there is any error in try block the control comes here otherwise not
            c) finally block    - it will gets executed whether there is exception occurs or not
        
        * there must be a except or finally block after a try block
        * except: block is mainly used to handle the exception occured in try block
        * we can specifically handle exceptions occured in try like following
            except <exception1>:
                <code>
            except <exception2>:
                <code>
            .
            .
            .
            else:
                # if no exceptions then this will gets executed
                <code>
            * raise keyword: 
                * if we use "raise" keyword then the
                  if there is a error then the next block of code after try, excpet, finally blocks will not gets executed.
                * when we use raise it will raise the error/exception and stops the program execution.

"""


# try except finally blocks
try:
    print(5/0)  # this leads to zerodividion exception/error
    # after exception raises the control will directly goes to the except block
    # the next code after exception will not be executed (following code will not gets executed)
    print("code after exception occurs")
except:
    # if there is error in try block then only the except block will gets executed otherwise it won't
    print("there is an exeption in try block")
    #raise  # this will tell about the exception occured in try block end of the program
finally:
    # the code in finally will always gets executed whether there is a exception or not 
    print("i'm finally i will always gets executed no matter what")


# if there is any error and if we raise that then the program will not run after finally
# if there is error above and if we dont raise it then this will gets executed
# raise means using "raise" keyword
print("hello")
# hanling different exceptions 
try:
    #print(1+'1') # this leads to TypeError
    #print(5/0)    # this leads to ZeroDivisionError
    print("no error")
except TypeError:
    # this will handle only TpyeError
    print("raised type error")
except ZeroDivisionError:
    print("raised zerodivision error")
except:
    # this will handle all the errors
    raise
else:
    print("no excetion raised so else block of code is getting executed")
finally:
    print("i'm finally i will always gets executed")


