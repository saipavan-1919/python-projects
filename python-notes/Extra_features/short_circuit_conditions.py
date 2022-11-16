"""
    Short circuit in conditions:
        ex1: if a>b and b>c:
        * in the above situation
            if the first statement (a>b) is false then it will not evaluate the second statement.
            because "and" will be true when both are true
        * if the first statement is true then it will surely evaluate the second statement.

        ex2: if a>b or b>c:
        * in this situation python
            if the first condition is true then it will not evaluate second statement.
            because "or" will be true either one statement is true
        * if the first statement is false then it will check the second statement

        We can use the short circuit to reduce the time complexcity of a program
        We need to use simple conditions first while evaluating any conditions

"""

a = 3
b = 4
c = 2

def foo():
    return 5
if a<b and c<b:
    print("hi")
else:
    print("bye")

# in below it will not evaluate the second statement
# this is the best way of writing statements in a condition
if a>b and c<foo():  # here first condition is false so it will not evaluate second statement
    print("hi")
else:
    print("bye")

if a<b or c<foo():  # here first condition is true so it will not evaluate second statement
    print("hi")
else:
    print("bye")

# in below code it will evaluate 
# this is not a good way to write the code
if b<foo() and a<b: # here it will evaluate two statements because first one is true
    print("hi")
else:
    print("bye")


