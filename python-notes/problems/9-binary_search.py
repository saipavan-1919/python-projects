# binary search
n = 4
a = [1,2,3,4,5,6,7,8,9,10,11]
l = 0
h = len(a)-1
m = (l+h)//2
count = 0
while a[m] != n:
    if n>a[m]:
        l=m+1
        m = (l+h)//2
    elif n<a[m]:
        h=m-1
        m = (l+h)//2
    elif n==a[m]:
        break
    count+=1
    print(l,h,m)

print(m,a[m],count)
