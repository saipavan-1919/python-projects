# 3) Write a Python program that matches a string that has an a followed by one or more b's.

import re

def a_followed_by_b(txt):
    # ^ - checks a string starts with that sequence or not
    # $ - checks a string ends with that specified sequence or not
    # () - used to group some characters
    # + - used to check it has 1 or more characters
    print(re.findall(r"^ab*$",txt))

    if re.search(r"^ab+$",txt):
        print("a is followed by one or more b's")
    else:
        print("a is not followed by b")

a_followed_by_b("a") # o/p = a is not followed by b
a_followed_by_b("ab") # o/p = a is followed by one or more b's
a_followed_by_b("abb") # o/p = a is followed by one or more b's
