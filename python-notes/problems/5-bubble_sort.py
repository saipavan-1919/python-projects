# Bubble sort

a = [5,4,2,1,3]
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
