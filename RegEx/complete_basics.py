import re

# findall method
# returns all the mathced strings as list
# with this we can count how many strings or characters presant in a string 
print(re.findall(r"a","hi how are you"))
print(re.findall(r" ","hi how are you"))


# search method
# search method returns a object
# search has 3 methods
# 1) start()   2) span()   3) string()
re_obj = re.search("are","hi how are you")
print(re_obj.start())    # gives the index of mathced string
print(re_obj.span())     # gives the span (start, stop) indexes as a tuple
print(re_obj.string)     # this gives the complete string


# sub method
# with this we can replace a string with another string inside a string
# re.sub(str1,str2,txt,count)  str1 is replaced by str2
print(re.sub("sai","pavan","sai pavan sai sai",2))


# split method
# split method splits the text at matched string and returns a list
# re.split(str,txt)
# txt is splitted at each matched str
print(re.split(" ","hi how are you"))


# [] is used for matching characters in a range 
print(re.findall("[1-9]","hi1234")) # gives only characters in range of 0-9 skips a-z characters
print(re.findall("[0-9][a-z]","1h22hh")) # mathces at 1 integer and 1 character adjacently

# matching 3 digits adjacent
# only mathces a string where there are 3 adjacent digits
# we need to understand it will match the string in first place if the same order characters presant in text
print(re.findall(r"[0-9][0-9][0-9]","123h12h1h")) 

# matching if a string starting with another string or not
print(re.findall("^my","my name is sai"))    # here finds a match
print(re.findall("^name","my name is sai"))  # here is no match
print(re.findall("^My","my name is sai"))    # case sensitive so no match

# matching if a string ends with another string or not
print(re.findall("sai$","my name is sai"))   # finds a match because the text ends with sai
print(re.findall("my$","my name is sai"))    # no match
print(re.findall("Sa$","my name is sai"))    # no match
print(re.findall("i$","my name is sai"))     # finds a match

# mathcing with any character in text
print(re.findall(".","hi my name is sai"))   # matches with all the characters
print(re.findall("h.","hi hoimy name is sai")) # finds a pattern where there can be any character after h
print(re.findall("h..p","hoop hoip help hece hfdh")) # finds a pattern there can be any two characters between h and p


print(re.findall("h*","hhi ice abc"))
print(re.findall("h{3}","hhh hh 22"))

# matching specified no.of occurences
# "h{3}" this will search for 3 adjacent occurence of h i.e == "hhh"
# "[a-z]{3}"  this equals to "[a-z][a-z][a-z]"  this will match any 3 adjacent characters
print(re.findall("h{3}","hhh hh 22"))
print(re.findall("[a-z]{3}","abc ab12cd ab defgh"))

# finding a number is valid or not
print(re.findall("[0-9]{10}","7013510804 70135108041"))
print(re.findall("[h-i]","hi hoi how help"))

print(re.findall("(22,hh)","hhh hh 22"))

# matching only with digits
print(re.findall("\d{2}","hi1234"))

# matching with non digits
print(re.findall("\D","hi1234"))

# matching from the starting of a string
print(re.findall(r"\Ahi","hi how are you")) # finds a match
print(re.findall(r"\Ahow","hi how are you")) # no match

# \b matches a string if they are at the begining or at the end of a word
print(re.findall(r"\byou","hi how are you"))  # mathces at end of word 
print(re.findall(r"\bar","hi how are you"))   # mathces at start of word
print(re.findall(r"\br","hi how are you"))  # no match because they are not at start or end

# \B matches a sequence of charecters are at the middle of a word.
print(re.findall(r"\Bo","hi how are you"))  # finds o because 'o' is at the middle of words
print(re.findall("\Bh","hi how are you"))   # no match because 'h' is at the begining of words

# matches where there is a white space character
print(re.findall(r"\s","hi how are you")) # finds only white space characters

# matches where there is no white space character
print(re.findall("\S","hi how are you")) # finds only no white space characters

# matches where there is a any character from [a-z][A-Z][0-9]_
# doesn't matches any other characters
print(re.findall("\w","hi how are yoy 1234 __")) # only matches a-z,A-Z,0-9,_

# mathces where there is no word characters
print(re.findall(r"\W","hi 1234 how are _ $%")) 

# matches if specified characters are at the end of the string
print(re.findall("\Zhi","hi how are you hi")) 
