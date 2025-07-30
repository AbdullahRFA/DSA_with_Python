"""
Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

Examples :

Input: LinkedList: 1->2->3->4->5 , x = 6
Output: 1->2->3->4->5->6
Explanation:

We can see that 6 is inserted at the end of the linkedlist.
Input: LinkedList: 5->4 , x = 1
Output: 5->4->1
Explanation:

We can see that 1 is inserted at the end of the linkedlist.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)


"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def append(self,arr):
        head = None
        tail = None
        for val in arr:
            new_node = Node(val)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        return head
    def traversal(self,head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

class Solution:
    def insertAtEnd(self, head, x):
        # code here
        new_node = Node(x)
        if not head:
            return new_node

        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

slv = Solution()
arr = [1,2,3,4,5]
sll = SLL()
head = sll.append(arr)
print("Before Inserting")
sll.traversal(head)

x = 6

slv.insertAtEnd(head,x)

print("After Inserting")
sll.traversal(head)



