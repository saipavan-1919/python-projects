# 12. Write a Python program that matches a word containing 'z'

import re

def word_with_z(txt):
    # \b - used to find a string at start or ending of a word
    # \B - used to find a string at the middle of a word (i.e not at the start or end of word)
    print(re.findall(r"\bz|\Bz",txt))
    if re.search(r"\bz|\Bz",txt):
        print("given words contains z")
    else:
        print("given words doen't contain z")

word_with_z("zezṇal")   # finds a match
word_with_z("hi hello") # no match
