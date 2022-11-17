import random

li = []
for i in range(10):
    li.append(random.randint(1,100))
print(li)
t = 1
index = 0
for i in li:
    li.remove(i)
    if i in li:
        t = 0
        break
    li.insert(index,i)
    index += 1

if t==0:
    print("there are some repeated elements")
else:
    print("unique elements")
 
