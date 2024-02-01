"""
    SETS:
    * sets are used to store mutiple values in a single variable.
    * sets are created with curly brackets.
      ex: my_set = set()
    * sets contains unique items.
    * There are no duplicate items in sets (elements are not repeated)
    * Set items are unordered, unchangeable(immutable), and do not allow duplicate values.
    * Unordered means that the items in a set do not have a defined order.
      Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
    * We cannot change the set items once they are created but we can add and remove items in a set.
    * We cannot use indexing to access a item in a set.

"""

# empty set declaration
my_set1 = set()
print(my_set1)
my_set2 = {}
print(my_set2)

# set initialization
my_set3 = set("123abc")
print(my_set3)
my_set4 = {1,2,3,4,5,'a','b','c','c'}
print(my_set4)

# length of a set
my_set5 = {1,2,3,4,5,6,5}
print(len(my_set5))

# accessing set items
# cannot access set items using indexing
set6 = {1,2,3,4,5}
print(set6)

# add items in set
set7 = {1,2,3,4}
set7.add(5)
print(set7)

# remove item from set
set8 = {1,2,3,4}
set8.remove(2)
print(set8)

# removing last item using pop
print(set8.pop())
print(set8)

# iterating through sets
for i in set8:
  print(i)

# union two sets
a = {1,2,3,4}
b = {4,5,6}
c = a.union(b)
print(c)

# intersection of two sets
d = a.intersection(b)
print(d)

# symmetric_difference_update
# keeps only which are not common
a = {1,2,3,4}
b = {4,5,6}
c = a.symmetric_difference(b)
print(c)
