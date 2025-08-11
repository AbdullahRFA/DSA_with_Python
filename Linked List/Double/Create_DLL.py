class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.head = None

    def insert(self,val):
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
        current = self.head
        while current:
            print(current.val,end="->")
            current= current.next


dll = DoubleLinkList()
dll.display_DLL()
dll.insert(10)
dll.display_DLL()



