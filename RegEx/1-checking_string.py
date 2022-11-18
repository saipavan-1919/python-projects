#1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

import re

# method 1
txt = "Sai1919 "
# \W mathces where the string does not contain any word characters
if re.search(r"\W",txt):
    print("txt contains other characters")
else:
    print("txt conatains only characters [a-z][A-Z][0-9]and _")


# method 2
txt = "Sai1919 "
# [^a-zA-Z0-9] it returns a match for the characters except that are in [] braces.
# ^ this is used to performs a exception
if re.search(r"[^a-zA-Z0-9_]",txt):
    print("other characters presant")
