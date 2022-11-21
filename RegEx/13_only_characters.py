# 13) Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores

import re

def only_chars(txt):
    # [^a] - it is used to find match except the characters inside braces []
     print(re.findall(r"[^a-zA-Z0-9_]",txt))
    if re.search(r"[^a-zA-Z0-9_]",txt):
        print("text contains unwanted characters")
    else:
        print("text contains only required characters")

only_chars("abcdeA123_") # finds match
only_chars("#$abc")      # no match
