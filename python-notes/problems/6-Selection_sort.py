# selection sort
"""
    In selection sort in every pass we find the least element in the array and we will place
    them from the starting of the array.

    if n elements are presant in a array then we require n-1 passes to sort.

    array =  [5, 3, 1, 2, 4]
    pass1 -> [1, 3, 5, 2, 4]
    pass2 -> [1, 2, 5, 3, 4]
    pass3 -> [1, 2, 3, 5, 4]
    pass4 -> [1, 2, 3, 4, 5]
"""

a = [5,3,1,2,4]

for i in range(len(a)-1):                   # passes = no.of elements - 1
    min_index = i                           # index of minimum element in list = index of pass
    for j in range(i,len(a)):               # passes = from i to last element
        if a[j] < a[min_index]:             # checking if current element less than min_ind variable
            min_index = j                   # making min_index to equal to cuurent elem index
    a[i],a[min_index] = a[min_index], a[i]  # swapping min_index and current pass index
    print(a)
print(a)    
