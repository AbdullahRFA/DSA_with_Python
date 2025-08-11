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
    def insert_at_nth_index(self, val,n):
        if not self.head or n == 0:
            self.insert_at_head(val)
            return
        else:
            new_node = Node(val)
            i = 0
            temp = self.head
            while temp and i<n-1:
                i+=1
                temp = temp.next
                
            if not temp:
                print("Index out of range")
                return
            else:
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
            

    def display_DLL(self):
        if not self.head:
            print("DLL does not create yet")
            return
        temp = self.head
        while temp.next:
            print(temp.val,end="->")
            temp= temp.next
        print(temp.val)
            
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next=new_node
            new_node.prev = temp
    def delete_head(self):
        if not self.head:
            print("DLL is empty")
            return
        elif not self.head.next:
            self.head = None
            return
        else:
            self.head = self.head.next
            return
    def delete_tail(self):
        if not self.head:
            print("DLL is empty")
            return
        elif not self.head.next:
            self.delete_head()
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        
    def delete_nth_element(self,n):
        if not self.head:
            print("DLL is empty")
            return
        if n==0:
            self.delete_head()
            return
        else:
            i = 0
            temp = self.head
            while temp and i<n-1:
                i+=1
                temp = temp.next
            if not temp or not temp.next:
                print("Out of index value")
                return
            else:
                temp.next = temp.next.next
        


dll = DoubleLinkList()
dll.display_DLL()
dll.create_DLL(1)
dll.create_DLL(2)
dll.create_DLL(3)
dll.create_DLL(4)
dll.display_DLL()
dll.insert_at_head(10)
dll.display_DLL()
dll.append(30)
dll.display_DLL()

dll.insert_at_nth_index(100,4)

dll.display_DLL()

dll.delete_head()
dll.display_DLL()

dll.delete_nth_element(6)
dll.display_DLL()

dll.delete_tail()
dll.display_DLL()




