"""
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head
        #
        # while curr:
        #     next_temp = curr.next     # Step 1: store next node
        #     curr.next = prev          # Step 2: reverse pointer
        #     prev = curr               # Step 3: move prev forward
        #     curr = next_temp          # Step 4: move curr forward
        #
        # return prev  # prev is new head now

        # Base case: if head is empty or only one node, return it
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Put current head after its next node
        head.next.next = head
        head.next = None  # disconnect the original forward link

        return new_head
