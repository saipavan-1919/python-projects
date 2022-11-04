# linked list
"""
    Single Linked List:
        We know that a linked list consist of nodes.
        Each node consist of two parts
            1) data of the node
            2) address of next node
        We need to maintain the head of the linked list to traverse through the linked list
        In this python based linked list each node will consist of two parts
            1) data of the node
            2) next node
        
        * In this programme i used two classed single_linked_list and node
           1) class single_linked_list:
           This class will contain the head of the linked list
           A method for displaying things in linked list
           2) class node:
           this class contains the data and the next node
           
"""

class single_linked_list:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next
    
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
ll = single_linked_list()
prev = ""
for i in range(4):
    n = node(int(input("enter input = ")))
    if ll.head==None:
        ll.head=n
    else:
        prev.next=n
    prev = n

ll.display()


