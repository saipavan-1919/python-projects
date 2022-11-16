"""
    Insertion sort:
        * Insertion sort starts from the 1st element in the array
        The current element will compared with the all previous elements and
        if the previous elements are lesser than the current element then they will be swapped
        swapping happens until the current element is inserted in currect place.
        
        * The current element should be placed in a location where all left side elements should
        be less than the current element and right side elements should be greater than the
        current element.

        * if there are n elements then it requires n-1 passes to sort in insertion sort

        array = [3,2,1,5,4]
                   |
        preocedure:
            pass 1:
            * The sorting starts by taking 1st element of the array = a[1] ==> 2
            * Then it should be compared with previous elements i.e a[0]
            * if a[0] is greatet than a[1] then a[1] and a[0] will be swapped
            pass1 = [2,3,1,5,4]
            pass 2:
            * The current element will become next element i.e, 2nd element = a[2] ==>1
            * Then current element will be compared with previous elements i.e, a[1], a[0]
            * If any of (a[1], a[0]) are bigger than a[2] then they need to be swapped
            pass2 = [1,2,3,5,4]
            pass 3:
            * current elemeent = a[3] = 5
            * previous elements are a[2],a[1],a[0]
            * if any previous elements are bigger than current element then should be swapped
                (here no previous elements are bigger than current element so no swaps will happen)
            pass 3 = [1,2,3,5,4]
            pass 4;
            * current elemeent = a[4] = 4
            * previous elements are a[3],a[2],a[1],a[0]
            * if any previous elements are bigger than current element then should be swapped
            pass4 = [1,2,3,4,5]
"""

a = [3,2,1,5,4]
print(a)
for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j] < a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
    print(a)
