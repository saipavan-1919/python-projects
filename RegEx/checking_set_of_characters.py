# this program is used to check for only certain characters are presant in the string or not
import re

txt = "a1fjd23A"
if len(re.findall("[^a-zA-Z0-9]",txt))==0:
    print("string contains only required characters")
