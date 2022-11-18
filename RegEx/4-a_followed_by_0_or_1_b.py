# 4) Write a Python program that matches a string that has an a followed by zero or one b's.

import re

def a_followed_by_b(txt):
    # ^ - checks a string starts with that sequence or not
    # $ - checks a string ends with that specified sequence or not
    # () - used to group some characters
    # ? - used to check either 0 or 1 character presant 
    print(re.findall(r"^ab?$",txt))

    if re.search(r"^ab?$",txt):
        print("a is followed by zero or one b")
    else:
        print("a is followed by more than 1 b's")

a_followed_by_b("a") # o/p = a is not followed by b
a_followed_by_b("ab") # o/p = a is followed by one or more b's
a_followed_by_b("abb") # o/p = a is followed by one or more b's
