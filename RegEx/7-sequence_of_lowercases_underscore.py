# 7) Write a Python program to find sequences of lowercase letters joined with a underscore

import re

def lower_underscore(txt):
    # [^arn] - this will print all characters except a,r,n
    # if we get any character other than a-z and _ then we can make decision based on that
    print(re.findall(r"[^a-z_]",txt))
    if re.search(r"[^a-z_]",txt):
        # if there is any match of other characters i.e
        print("the string is not formed by lower letters [a-z] and underscore")
    else:
        # if there are no mathces of other characters then
        print("the string is just formed by lower letters [a-z] and underscore")


lower_underscore("Abc_hi")
lower_underscore("abc_hi")
