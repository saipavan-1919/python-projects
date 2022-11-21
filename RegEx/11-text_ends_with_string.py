# 11. Write a Python program that matches a word at the end of string, with optional punctuation.

import re

def ends_string(sstr,txt):
    print(re.findall(f"{sstr}$",txt))     # method 1
    print(re.findall(f"{sstr}\Z",txt))    # method 2
    if re.findall(f"{sstr}\Z",txt):
        print("text ends with string")
    else:
        print("text doesn't ends with string")

ends_string("hi","hi everyone hi") # finds match
ends_string("e","abcde")           # finds match
ends_string("e","abcdef")          # no match
