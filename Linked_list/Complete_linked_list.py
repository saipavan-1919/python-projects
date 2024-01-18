"""
    Linked list:
        Creating a linked list
        traversing the linked list
        adding node at the end of linked list
        adding node at the begining of the linked list
        removing node at the end of the linked list
        remocing node at the begining of the linked list
        
"""

class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def create_linked_list(self):
        # this function creates a linked list
        print(f"Creating linked list")
        prev_node = None
        node = None
        for i in range(5):
            node = Node()
            node.data = i
            if self.head == None:
                self.head = node
            else:
                prev_node.next = node
            prev_node = node
    def traverse_linked_list(self):
        # this function traverse through linked list
        print(f"traversing through the linked list")
        temp_head = self.head
        while temp_head:
            print(temp_head.data,end="")
            temp_head = temp_head.next
        print()
    def add_node_end(self):
        # this function adds the node at the end of linked list
        print(f"adding node at the end to the linked list")
        temp_head = self.head
        while temp_head.next:
            temp_head = temp_head.next
        temp_head.next = Node()
        temp_head.next.data = temp_head.data + 1
    def add_node_start(self):
        # this function adds node at start of linked list
        print(f"adding node at beginning of linked list")
        node = Node()
        node.next = self.head
        self.head = node
        self.head.data = self.head.next.data -1 
    def rem_node_end(self):
        # this function removes node at the end of linked list
        print(f"removing node at the end of the linked list")
        temp_head = self.head
        prev_node = Node
        while temp_head.next:
            prev_node = temp_head
            temp_head = temp_head.next
        prev_node.next = None
    def rem_node_start(self):
        # this function removes the node at the start of linked list
        print(f"removing node from the start of linked list")
        self.head = self.head.next
    def add_node_pos(self,pos):
        # this function adds nodes at a particular position
        print(f"adding node at pos: {pos}")
        if pos == 0:
            self.add_node_start()
            return
        temp_head = self.head
        temp_pos = 0
        while temp_pos < pos - 1:
            temp_head = temp_head.next
            temp_pos += 1
        node = Node()
        node.data = 9
        node.next = temp_head.next
        temp_head.next = node
    def rem_node_pos(self,pos):
        # this function removes the node at a particular position
        print(f"removing node at pos: {pos}")
        if pos == 0:
            self.rem_node_start()
            return
        temp_pos = 0
        temp_head = self.head
        next_node = temp_head.next
        while temp_pos < pos - 1:
            temp_head = temp_head.next
            next_node = temp_head.next
            temp_pos += 1
        temp_head.next = next_node.next

def main():
    # creating linked list
    ll = LinkedList()
    ll.create_linked_list()
    ll.traverse_linked_list()
    ll.add_node_end()
    ll.traverse_linked_list()
    ll.rem_node_end()
    ll.traverse_linked_list()
    ll.rem_node_start()
    ll.traverse_linked_list()
    ll.add_node_pos(0)
    ll.traverse_linked_list()
    ll.rem_node_pos(2)
    ll.traverse_linked_list()


if __name__ == "__main__":
    main()
