

"""
    Strings:
        strings are one of the python objects.
        string is collection of characters.
        strings are declared using single or double quotation marks.
        syntax: 
            str1 = "hi i'm a string"      # here we can print single quotations but not double quotations
            str2 = 'hi im also a string' # here we can print double quotation but not single quotations
        
        * we can access the string elements using indexing str1[index]
            it will give the element at the index position
        * strings are immutable and ordered
        * immutable means we cannot change them through indexing.
        * 
"""
# string declaration
str1 = "hi i'm a string"       # we can print single quotations not double quotations
str2 = 'hi i am a string "hi"' # we can print double quotaions not single quotations
print(str1)
print(str2)

# using escape sequences
# escape sequence is used to print any character 
# escape sequence starts with a backslash ('\')
str1 = 'hi i\'m a string'  # to print single quote we need to use backslash before single quote \'
print(str1)
str2 = "\"hi\""
print(str2)

# to ignore escape sequence we need to take the string with in r"" format
# it is known as raw string format
# it will print the string as it is without any changes
str3 = r"\'hi\'" 
print(str3)

# accessing through indexing
# string elements start from 0th index and goes upto length-1
str4 = "hello world"
print(str4[0])  # str4[0] -> 'h'
print(str4[1])  # str4[1] -> 'e'
# we can also use negative indexes 
# negative indexing is used to access elements from last of the string
# -1 refers to last element
# -2 refrs to last second element
# -3 refers to last third element
print(str4[-1])  # this will give last element of the string str4[-1] -> 'd'
print(str4[-2]) # str4[-2] ->'l'

# slicing of string
# we can slice that means we can cut the strings into parts using slicing
# syntax for slicing : string[start:stop]
# by default start = 0, stop = len-1
# it will give the string from index start to stop-1
str5 = "hello world"
print(str5[0:2])  # gives string from oth index to 1st index
print(str5[:5])   # directly gives upto 5th index

# step in strings
# used to take those many gaps between each index
# index is incremented by step size
# syntax for step : string[start:stop:step]
# by default step = 1
str6 = "hey how are you"
print(str6)       # its step size is 1 index is incremented by 1
print(str6[::2])  # its step size is 2 index is incremented by 2
# reversing string
print(str6[::-1]) # its step size is -1 index is decremented by 1 every time


# formatting of strings
# we can format strings in two ways 
# 1) .format (dot format method)   2) f""  (f string method)

# .format
# printing in a sequence
print("{} {}".format("hi","hey"))
# printing in required order
print("{1} {0}".format)


# fstring format
