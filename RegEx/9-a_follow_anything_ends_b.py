# 9) Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re


def start_a_end_b(txt):
    print(re.findall(r"^a[a-z]*b$",txt))
    if re.search(r"^a[a-z]b$",txt):
        print("text starts with a and ends with b")
    else:
        print("text is not matching required pattern")

start_a_end_b("abcdb") # finds a match
start_a_end_b("abc")   # no match
start_a_end_b("ab")    # finds a match
