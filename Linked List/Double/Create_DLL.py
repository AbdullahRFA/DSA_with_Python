# Node class for a Doubly Linked List (DLL)
class Node:
    def __init__(self, val):
        self.val = val        # Value stored in the node
        self.next = None      # Pointer to the next node in the list
        self.prev = None      # Pointer to the previous node in the list

# Doubly Linked List class
class DoubleLinkList:
    def __init__(self):
        self.head = None      # Head (first) node of the list
        self.current = None   # Helper pointer to keep track of last inserted node (used in create_DLL)

    # Create DLL by adding nodes sequentially at the end
    def create_DLL(self, val):
        new_node = Node(val)  # Create a new node
        if not self.head:     # If list is empty
            self.head = new_node
            self.current = new_node
        else:                 # If list already has elements
            self.current.next = new_node  # Link current last node to new node
            new_node.prev = self.current  # Link new node back to current
            self.current = new_node       # Update current to new node

    # Insert a node at the head of DLL
    def insert_at_head(self, val):
        new_node = Node(val)  
        if not self.head:             # If DLL is empty
            self.head = new_node
        else:                         # If DLL has elements
            new_node.next = self.head # Link new node to old head
            self.head.prev = new_node # Link old head back to new node
            self.head = new_node      # Update head to new node

    # Insert a node at a given nth index (0-based index)
    def insert_at_nth_index(self, val, n):
        if not self.head or n == 0:  # If DLL is empty OR inserting at head
            self.insert_at_head(val)
            return
        else:
            new_node = Node(val)
            i = 0
            temp = self.head
            # Traverse to node just before target position
            while temp and i < n-1:
                i += 1
                temp = temp.next
                
            if not temp:  # If index out of range
                print("Index out of range")
                return
            else:
                # Link new node with next and prev pointers
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next:               # If not inserting at tail
                    temp.next.prev = new_node
                temp.next = new_node

    # Display the DLL from head to tail
    def display_DLL(self):
        if not self.head:
            print("DLL does not create yet")
            return
        temp = self.head
        # Traverse until last node
        while temp.next:
            print(temp.val, end="->")
            temp = temp.next
        print(temp.val)  # Print last node value

    # Append node at the tail of DLL
    def append(self, val):
        new_node = Node(val)
        if not self.head:       # If list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:    # Move to last node
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp  # Link new node to last node

    # Delete head node of DLL
    def delete_head(self):
        if not self.head:
            print("DLL is empty")
            return
        elif not self.head.next:  # Only one node
            self.head = None
            return
        else:
            self.head = self.head.next  # Move head pointer to next node
            self.head.prev = None       # Remove back link

    # Delete tail node of DLL
    def delete_tail(self):
        if not self.head:
            print("DLL is empty")
            return
        elif not self.head.next:  # Only one node
            self.delete_head()
        else:
            temp = self.head
            while temp.next:      # Move to last node
                temp = temp.next
            temp.prev.next = None # Remove link to last node

    # Delete nth node from DLL (0-based index)
    def delete_nth_element(self, n):
        if not self.head:
            print("DLL is empty")
            return
        if n == 0:               # If deleting head
            self.delete_head()
            return
        else:
            i = 0
            temp = self.head
            while temp and i < n-1:  # Move to node before target
                i += 1
                temp = temp.next
            if not temp or not temp.next:  # If index out of range
                print("Out of index value")
                return
            else:
                target = temp.next
                temp.next = target.next  # Skip the target node
                if target.next:          # If target is not last node
                    target.next.prev = temp


# ------------------ DEMO ------------------
dll = DoubleLinkList()

dll.display_DLL()               # DLL does not create yet
dll.create_DLL(1)               # Create DLL with 1
dll.create_DLL(2)               # Append 2
dll.create_DLL(3)               # Append 3
dll.create_DLL(4)               # Append 4
dll.display_DLL()               # 1->2->3->4

dll.insert_at_head(10)          # Insert at head
dll.display_DLL()               # 10->1->2->3->4

dll.append(30)                  # Append at tail
dll.display_DLL()               # 10->1->2->3->4->30

dll.insert_at_nth_index(100, 4) # Insert at index 4
dll.display_DLL()               # 10->1->2->3->100->4->30

dll.delete_head()                # Delete head
dll.display_DLL()               # 1->2->3->100->4->30

dll.delete_nth_element(6)        # Attempt out-of-range delete
dll.display_DLL()               # List remains unchanged

dll.delete_tail()                # Delete tail
dll.display_DLL()               # 1->2->3->100->4