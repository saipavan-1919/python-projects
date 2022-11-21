# 10. Write a Python program that matches a word at the beginning of a string.

import re

def beg_string(s_str,txt):
    # \A - used to match if text starts with string
    # ^ - also used to match if text starts with string 
    print(re.findall(f"\A{s_str}",txt))  # method 1
    if re.search(f"^{s_str}",txt):       # method 2
        print("text starts with the string")
    else:
        print("text doesn't starts with string")

beg_string("hi","hi hello") # finds a match
beg_string("a","abcd")      # no match
beg_string("b","abcd")      # no match
