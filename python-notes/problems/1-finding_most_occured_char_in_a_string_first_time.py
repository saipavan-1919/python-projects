# This program will find the most occured character in a string for the first time.

str2 = "Hello world Ho!!!"
my_dict = {}
li = []
for i in str2:
    if i not in li:
        my_dict[i] = 0
    for j in str2:
        if i==j and (i not in li):
            my_dict[i] = my_dict[i] +1
    li.append(i)

print(my_dict)
val = 0
key = 0
for k,v in my_dict.items():
    if v>val:
        val=v
        key=k
print(val,key)
