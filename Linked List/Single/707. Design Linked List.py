"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3



"""
"""
1. get(index)
    Start from the head and move to the next node index times.
    If you reach the desired index, return its value; otherwise, return -1.
    
2. addAtHead(val)
    Create a new node.
    Set its next pointer to the current head.
    Update the head to this new node.
    
3. addAtTail(val)
    Move to the end (last node) of the list.
    Set the next pointer of the last node to the new node.
    
4. addAtIndex(index, val)
    Move to the node just before the target index.
    Insert the new node by adjusting pointers.
    Special case: if index is 0, use addAtHead.
    
5. deleteAtIndex(index)
    Move to the node just before the target index.
    Bypass the node to delete by adjusting pointers.
    Special case: if index is 0, move head pointer to the next node.

"""

class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = node(val)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            new_node = node(val)
            temp = self.head

            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
Here’s a detailed explanation of each method in your MyLinkedList class, including what it does and how it works:

⸻

✅ Class: node

class node:
    def __init__(self, val):
        self.val = val
        self.next = None

	•	Represents a single node in a singly linked list.
	•	val stores the data.
	•	next points to the next node in the list (or None if it’s the last node).

⸻

✅ Class: MyLinkedList

This class implements a singly linked list with standard operations.

🔹 __init__(self)

def __init__(self):
    self.head = None
    self.size = 0

	•	Initializes an empty linked list.
	•	head points to the first node of the list.
	•	size tracks the number of elements in the list.

⸻

✅ get(self, index)

def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
        return -1
    temp = self.head
    for _ in range(index):
        temp = temp.next
    return temp.val

	•	Returns the value at the specified index.
	•	If index is invalid (negative or out of bounds), returns -1.
	•	Starts at head and traverses the list until the desired index.

⏱️ Time complexity: O(n)

⸻

✅ addAtHead(self, val)

def addAtHead(self, val: int) -> None:
    new_node = node(val)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

	•	Inserts a new node at the beginning of the list.
	•	The new node becomes the new head.
	•	Increments the size.

⏱️ Time complexity: O(1)

⸻

✅ addAtTail(self, val)

def addAtTail(self, val: int) -> None:
    new_node = node(val)
    if not self.head:
        self.head = new_node
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    self.size += 1

	•	Appends a node at the end of the list.
	•	If the list is empty, the new node becomes the head.
	•	Otherwise, traverses to the last node and links the new node there.

⏱️ Time complexity: O(n)

⸻

✅ addAtIndex(self, index, val)

def addAtIndex(self, index: int, val: int) -> None:
    if index == self.size:
        self.addAtTail(val)
        return
    elif index > self.size:
        return
    elif index == 0:
        self.addAtHead(val)
    else:
        new_node = node(val)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

	•	Inserts a node at a specific index:
	•	If index == size, inserts at the tail.
	•	If index > size, does nothing.
	•	If index == 0, inserts at the head.
	•	Otherwise, finds the (index-1)th node, and inserts the new node after it.

⏱️ Time complexity: O(n)

⸻

✅ deleteAtIndex(self, index)

def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.size:
        return
    if index == 0:
        self.head = self.head.next
        self.size -= 1
    else:
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        self.size -= 1

	•	Deletes the node at the specified index.
	•	If the index is invalid, does nothing.
	•	If deleting head (index 0), update head to the next node.
	•	Otherwise, skip the node at index by adjusting the .next pointer.

⏱️ Time complexity: O(n)

⸻

✅ Summary Table

Method	Action	Time Complexity
get(index)	Get value at index	O(n)
addAtHead(val)	Insert at beginning	O(1)
addAtTail(val)	Insert at end	O(n)
addAtIndex(i,v)	Insert at given index	O(n)
deleteAtIndex(i)	Delete node at index	O(n)


⸻

If you’d like, I can help you implement a printList() method to visualize the list too.

"""