"""
You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

Example1:

Input:
2<->2<->10<->8<->4<->2<->5<->2
2
Output:
10<->8<->4<->5
Explanation:
All Occurences of 2 have been deleted.

Example2:

Input:
9<->1<->3<->4<->5<->1<->8<->4
9
Output:
1<->3<->4<->5<->1<->8<->4
Explanation:
All Occurences of 9 have been deleted.
Your Task:

Complete the function void deleteAllOccurOfX(struct Node** head_ref, int key), which takes the reference of the head pointer and an integer value key. Delete all occurrences of the key from the given DLL.

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(1).

Constraints:

1<=Number of Nodes<=105

0<=Node Value <=109
"""

# User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''


class Solution:
    # Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        if not head:
            return None
        current = head
        while current and current.data == x:
            current = current.next

        if not current:
            return None

        head = current
        head.prev = None

        curr = head

        while curr:
            if curr.data == x:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                curr = curr.next
            else:
                curr = curr.next
        return head