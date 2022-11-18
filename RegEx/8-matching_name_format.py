# 8) Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

def capital_lowercase(txt):
    # here we are matching with one capital letter and all small letters
    # ^ - mathces a string which starts with sequence
    # [] - is used for range of characters
    # + - used for one or more occurence ex: b+ it will match b or bb or bbb...b 
    print(re.findall(r"^[A-Z][a-z]+",txt))
    if re.search(r"^[A-Z][a-z]+",txt):
        print("The name is in correct format")
    else:
        print("the name is not in correct format")

capital_lowercase("Sai")
capital_lowercase("sai")
