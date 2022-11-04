# list comprehension
"""
    Advantages of List Comprehension
    * More time-efficient and space-efficient than loops.
    * Require fewer lines of code.
    * Transforms iterative statement into a formula.
"""
li = [i for i in range(6) if i%2==0]
print(li)


# pop in lists
li = [1,2,3,4]
print(li.pop()) # pops last item in list
print(li.pop(0)) # pop 0th item in list 
print(li.pop(1)) # pops 1st item in list

# removing key value pair from dictionary
di = {'1':1, '2':2, 'a':'hi'}
di.__delitem__('a')  # removes key value pair with key = 'a' from di
print(di)


# creating a class of car
class car:
    def __init__(self,brand,model,colour):
        self.brand = brand
        self.model = model
        self.colour = colour

car1 = car("suzuki","swift","silver")
print(f"my car company is {car1.brand},my car model name is {car1.model}, and my car colour is {car1.colour}")
