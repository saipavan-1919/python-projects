"""
    Generator:
        Generator is a function which uses yield keyword instead of return.
        * if the body of the function consist of yield then that function is known as generator.
        Yield:
            yield keyword used to make a function as a generator.
            yield returns a generator object.
            A generator object can be iterated.
        * we can use iteration or next method to iterate through a generator function/object.
        * 
"""
# generator function
def gen1():
    for i in range(5):
        yield i

# creating a generator object
a = gen1()

# iterating through generator using next method
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# iterating through genrator using for loop
for i in gen1():
    print(i)

# my range generator function
def my_range(n):
    i=0
    while i<n:
        yield i
        i=i+1

for i in my_range(5):
    print(i)
