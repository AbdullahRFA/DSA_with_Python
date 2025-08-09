"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?


"""

"""
⸻

1. Brute Force Approach

Idea:
	•	First, find the total length of the linked list.
	•	Then, figure out which node to delete by calculating its position from the start:
position_from_start = length - n
	•	Traverse again and remove that node.

Steps:
	1.	Traverse the list once to get its length.
	2.	If n == length, that means we’re removing the first node — just return head.next.
	3.	Otherwise, traverse again until you reach the node just before the one you want to remove.
	4.	Change the .next pointer to skip the target node.

Time Complexity:
	•	First traversal = O(L)
	•	Second traversal = O(L)
	•	Total: O(2L) ≈ O(L)
Space Complexity: O(1)

⸻

2. Optimal Approach (Two-Pointer / Fast & Slow)

Idea:
	•	Use two pointers (fast and slow) so you only traverse once.
	•	Maintain a gap of n nodes between them.
	•	When fast reaches the end, slow will be just before the node to delete.

Steps:
	1.	Set fast = head and slow = head.
	2.	Move fast forward n times.
	3.	If fast is now None, that means the node to remove is the head — return head.next.
	4.	Otherwise, move both pointers one step at a time until fast.next becomes None.
	5.	Delete the node after slow by doing slow.next = slow.next.next.

Time Complexity: O(L) (one pass)
Space Complexity: O(1)

⸻

✅ Why optimal is better:
	•	Only one pass instead of two.
	•	Still O(1) space.
	•	Cleaner logic for large lists.

⸻
"""
from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # current = head
        # ln = 0
        # while current:
        #     ln += 1
        #     current = current.next
        # # print(n)
        # if n==1 and ln ==1:
        #     return None
        # ln = ln-n

        # if ln == 0:
        #     head = head.next
        #     return head
        # # print(ln)
        # i=1
        # current = head
        # while i<ln:
        #     current = current.next
        #     i+=1

        # current.next = current.next.next

        # return head

        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head