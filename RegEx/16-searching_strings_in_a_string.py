"""
    16) Write a Python program to search some literals strings in a string. Go to the editor
    Sample text : 'The quick brown fox jumps over the lazy dog.'
    Searched words : 'fox', 'dog', 'horse'
"""


import re


def literal_strings(patterns,txt):
    for pattern in patterns:
        if re.search(pattern,txt):
            print(f"{pattern} matched")
        else:
            print(f"{pattern} is not matched")


literal_strings(['fox', 'dog', 'horse'],"The quick brown fox jumps over the lazy dog.")
