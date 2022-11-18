# 5)  Write a Python program that matches a string that has an a followed by three 'b'

import re

def a_followed_by_3_b(txt):
    # ^ - checks a string starts with that sequence or not
    # $ - checks a string ends with that specified sequence or not
    # {} - matches number of specified occurences
    print(re.findall(r"^ab{3}$",txt))
    if re.search(r"^ab{3}$",txt):
        print("a is followed by 3b's")
    else:
        print("a is not followed by 3 b's")

a_followed_by_3_b("abbb") # o/p = a is followed by 3 b's
a_followed_by_3_b("ab")   # o/p = a is not followed by 3 b's 
a_followed_by_3_b("abc")  # o/p = a is not followed by 3 b's
