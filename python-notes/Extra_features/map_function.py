"""
    Map function:
        map function takes two arguments 
        1) function 2) iterator
        it will apply/run the function for all the values in the iterator and returns a map object.
        syntax:     <map_object> map(<function>, <iterator>)

"""

li = ['1','2','3','4']
o = map(int,li)
print(o)
# iterating through the map object using for loop
for i in o:
    print(i)

# converting all values using the list function
print(list(map(int,li)))
