"""
  this program will split the cards into two pairs randomly
  it will check whose top card has higher value
  who has the higher value they will receive both cards and those cards will be placed in the  last
  the game will continue until one lost all his cards.
"""

l = [1,2,3,4,5,6,7,8,9,10]
print(l)
from random import shuffle
shuffle(l)
print(l)
l1 = []
l2 = []
i =True
for item in l:
    if i:
        l1.append(item)
        i=False
    else:
        l2.append(item)
        i=True

print(l1)
print(l2)
while True:
    if l1[0] < l2[0]:
        t1 = l1.pop(0)
        t2 = l2.pop(0)
        l2.append(t2)
        l2.append(t1)
    elif l1[0] > l2[0]:
        t1 = l1.pop(0)
        t2 = l2.pop(0)
        l1.append(t1)
        l1.append(t2)
    print(l1)
    print(l2)
    print("\n")
    if len(l1) == 0:
        print("user 2 is the winner")
        break
    elif len(l2)==0:
        print("user 1 is the winner")
        break
