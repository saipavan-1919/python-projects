# conditional operator in python
# conditional operator is a terinary operator
# in c conditional operator is = ?:
# but in python its syntax is little different i.e,
# v = "val1" if <condition> else <val2>
# if condition is true then v will get "val1"
# if condition is falase then v will get "val2"

a = 2
b = 3

val = "b is big" if b>a else "a is big"
print(val)

a = 6
b = 5
val = "b is big" if b>a else "a is big"
print(val)

signal = "red"
action = "stop" if signal=="red" else "go"
print(action)
