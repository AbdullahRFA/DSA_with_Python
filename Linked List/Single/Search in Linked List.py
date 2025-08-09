"""
Given a linked list of n nodes and a key, the task is to check if the key is present in the linked list or not.

Example:

Input: n = 4, key = 3
1->2->3->4
Output: true
Explanation: 3 is present in Linked List, so the function returns true.
Constraint:
1 <= n <= 105
1 <= key <= 105
"""
# User function Template for python3


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:
    def searchKey(self, n, head, key):
        # Code here

        current = head
        found = False

        while current is not None:
            if current.data == key:
                found = True
                return found
            current = current.next
        return found

