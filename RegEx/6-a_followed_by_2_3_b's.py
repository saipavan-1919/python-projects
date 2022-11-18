# 6)  Write a Python program that matches a string that has an a followed by two to three 'b

import re

def a_follow_by_2_to_3_b(txt):
    print(re.findall(r"ab{2,3}",txt))  # method 1 = r"ab{2,3}"
    if re.search(r"ab{2}|ab{3}",txt):  # method 2 = r"ab{2}|ab{3}"
        print("a followed by 2 to 3 b's")
    else:
        print("a is not followed by 2-3 b's")

a_follow_by_2_to_3_b("ab") # o/p = a is not followed by 2-3 b's
a_follow_by_2_to_3_b("abbb") # o/p = a followed by 2 to 3 b's
a_follow_by_2_to_3_b("abbbb") # o/p = a is followed by 2-3 b's
