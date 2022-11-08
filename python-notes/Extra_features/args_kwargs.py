# using args 
def func(*args):
    for i in args:
        print(i)
    print(args)
    print(type(args))

func(1,2,3,"hi","how")

# using **kwargs
def func2(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
    print(kwargs)
    print(type(kwargs))

func2(a=1,b=2,c=3)

