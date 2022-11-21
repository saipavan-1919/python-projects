# 17) Write a Python program to replace whitespaces with an underscore and vice versa.

import re


def replace_space_underscore(txt):
    txt = re.sub(" ","_",txt)
    print("replaced whitespaces with underscore in txt",txt)
    txt = re.sub("_"," ",txt)
    print("replaced underscore with whitespaces in txt",txt)

replace_space_underscore("hi my name is sai_pavan")
