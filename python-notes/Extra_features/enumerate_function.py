# enumerate fuction
"""
    when iterating through a iterable object then we need to keep a eye on the count of elements.
    To make it easier for us(programmers) python has a inbuilt function called enumerate function.
    
    syntax:
        <enumerate_object> enumerate(iterable, start=0)

        * it takes iterable object as argument
        * returns the enumeratable object 
        * start is used to make the count start from that number
        * we can iterate through the returned object using for loops
        * we can also use list() method to make it as a list 

"""

li = [1,2,3,4]
o = enumerate(li)
for i in o:
    print(i)

# making the enumerate as a list
print(list(enumerate(li)))

# start parameter
o1 = enumerate(li,start=23)
for i in o1:
    print(i)
