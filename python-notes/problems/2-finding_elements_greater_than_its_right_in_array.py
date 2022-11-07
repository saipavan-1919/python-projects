'''finding the elements in an array which are greater than its 
right most values like a[]={27,5,17,4,25,9,2,3}
output: b[]={27,17,25,9} '''

a = [27,5,17,4,25,9,2,3]
i=0
li = []
while i<len(a)-1:
    if a[i]>a[i+1]:
        li.append(a[i])
    i=i+1

print(li)
