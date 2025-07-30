

class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def traversal(self):
        if not self.head:
            print("SLL is empty")
        current = self.head
        while current is not None:
            print(current.val,end=" ")
            current = current.next
        print()
    def insert(self,pos,val):
        new_node = node(val)
        if not self.head:
            self.head = new_node
        elif pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = None
            current = self.head
            count = 0
            # for _ in range(1,pos):
            #     previous = current
            #     current = current.next
            # previous.next = new_node
            # new_node.next = current

            while current is not None and count < pos:
                previous = current
                current = current.next
                count +=1

            previous.next = new_node
            new_node.next = current
    def delete(self,val):

        if self.head.val == val:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            found = False
            previous = None
            current = self.head

            while current is not None:
                if current.val == val:
                    found = True
                    break
                previous = current
                current = current.next
            if found:
                previous.next = current.next
                del current
            else:
                print("Not Found")


Sll = SingleLinkedList()
Sll.append(190)
Sll.append(19)
Sll.append(170)
Sll.append(13)
Sll.traversal()
Sll.insert(10,30)
Sll.traversal()
Sll.delete(170)
Sll.traversal()
Sll.delete(40)
Sll.traversal()
