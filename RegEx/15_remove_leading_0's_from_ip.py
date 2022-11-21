# 15) Write a Python program to remove leading zeros from an IP address.


import re

def rem_leading_zeros_ip(ip):
    # <character>+ - used to find one or more occurences of the character
    # re.sub(str1,str2,txt,count)
    # sub method replaces str1 with str2 count no.of times in txt.
    # sub returns the replaced text
    print(re.findall(".0+",ip))
    ip = re.sub(".0+",".",ip)
    print("successfully removed leading zeros from ip ", ip)

rem_leading_zeros_ip("216.08.094.196")
rem_leading_zeros_ip("216.008.094.000196")
