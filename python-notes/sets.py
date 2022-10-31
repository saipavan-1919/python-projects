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