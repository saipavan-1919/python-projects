# range
def my_range(*args):
    l = len(args)
    if l==1:
        start = 0
        stop = args[0]
        step = 1
    elif l==2:
        start = args[0]
        stop = args[1]
        step = 1
    elif l==3:
        start = args[0]
        stop = args[1]
        step = args[2]
    while (start<stop and step>0) or (start>stop and step<0):
        start += step
        yield start-step

for i in my_range(5,1,-1):
    print(i)
