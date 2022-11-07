# quick sort

a = [3,4,5,2,6,7,9,8,1]
i=0;j=0;
t=0
while i<len(a):
    j=0
    while j<len(a)-i-1:
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
        j=j+1
    i=i+1

print(a)
