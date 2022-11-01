"""
    RegEx (Regular expressions):
    RegEx are used to identify a pattern in a string.
    RegEx Module:
        Main methods in RegEx module are
        1) findall - Returns a list containing all matches
        2) search  - Returns a matched object or None
        3) split   - Returns a list where the string is split at each match 
        4) sub     - Replaces one or many matches with a string
    
    \w - {a-zA-Z0-9_}
    \W - {^a-zA-Z0-9_}
    \s - white spaces
    [] - to specify some range
    {} - Exactly the specified number of occurrences
    .  - any character
    [^]-Returns a match for any character EXCEPT a, r, and n


"""
import re

text = "Hi, How are you. HI!"

# findall method
print(re.findall(r"H.", text))

# search method
print(re.search("Hi",text))   # returns first matched object
print(re.search("Hoi",text))  # returns none

# finding multiple patterns with some common terms
txt = "sat, hat, mat, pat"
print(re.findall(r'[sh]at',txt))

# finding all patterns that starts with a different letter
print(re.findall(".at",txt))  # . is used to represant any character

# using range
print(re.findall("[i-z]at",txt)) # excludes hat because h is not in range of [i-z]

# using not in range
print(re.findall("[^i-z]at",txt)) # this will exclude sat, mat and pat

# re.compile method
# We can combine regular expression patterns into objects which can be used for pattern matching
txt = "hi my name is sai"
#print(re.sub("my", "mine", txt)) # this will replace the my with mine
obj1 = re.compile("my") # this creates a expression pattern object of string "my"
print(obj1.sub("hi",txt)) # this will replace the string "my" with "hi" in txt and returns new string

# matching all the integers
txt = "12abc4s5"
print(re.findall(r"\d",txt))

# matching all non integers (non numbers)
print(re.findall("\D",txt))

# matching specified number of occurences
txt = " 222-222-1212"
print(re.search(" \w{3}-\w{3}-\w{4}",txt))

# matching using a range of characters
name = "sai pavan"
# "\w{2,10}"  this represants characters can be from 2 to 10 places
#
if re.search("\w{2,10}\s\w{2,10}",name):
    print("It is a proper name")               
