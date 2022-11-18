# 2)  Write a Python program that matches a string that has an 'a' followed by zero or more b's

import re

txt = "a"
# ^ - checks a string starts with that sequence or not
# $ - checks a string ends with that specified sequence or not
# () - used to group some characters
print(re.findall(r"^ab*$",txt))

if re.search(r"^ab*$",txt):
    print("a is followed by zero or more b's")
else:
    print("a is followed by something else")
