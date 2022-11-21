# 14) Write a Python program where a string will start with a specific number

import re

def start_with_number(num,txt):
    print(re.findall(f"^{num}",txt))
    if re.search(f"^{num}",txt):
        print("the text starts with the required number")
    else:
        print("the text doesn't starts with required number")

start_with_number(7,"6789") # no match
start_with_number(9,"9346") # finds match
start_with_number(123,"123456789") # finds match
