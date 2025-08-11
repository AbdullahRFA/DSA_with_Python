
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.current = None
    def create_DLL(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node



    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display_DLL(self):
        if not self.head:
            print("DLL does not create yet")
            return
        temp = self.head
        while temp:
            print(temp.val,end="->")
            temp= temp.next


dll = DoubleLinkList()
dll.display_DLL()
dll.create_DLL(1)
dll.create_DLL(2)
dll.create_DLL(3)
dll.create_DLL(4)
dll.display_DLL()
# dll.insert_at_head(10)
# dll.display_DLL()



