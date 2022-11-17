# pairs of a given array A whose sumvalue is equal to a target value N

import random

num_list = []
for i in range(10):
    num_list.append(random.randint(1,20))
print(num_list)
n = 10

for i in range(len(num_list)-1):
    for j in range(i+1,len(num_list)):
        if num_list[i] + num_list[j] == n:
            print(num_list[i],num_list[j])
