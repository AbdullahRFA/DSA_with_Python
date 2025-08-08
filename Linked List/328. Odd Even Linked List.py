"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""
"""
💡 Brute Force Approach (Your Initial Attempt)

Technique:
	1.	Traverse and collect odd-indexed nodes’ values in a list.
	2.	Traverse again and collect even-indexed nodes’ values.
	3.	Concatenate both.
	4.	Rewrite values in the original list node-by-node.

Time Complexity: O(N)

Space Complexity: O(N) (uses an extra list)

Pros:
	•	Simple and intuitive.

Cons:
	•	Not space-efficient. Doesn’t take advantage of the linked list structure.
	•	Modifies node values instead of pointers.

⸻

✅ Optimal Approach (In-Place Pointer Manipulation)

Technique:
	1.	Split the list into two parts:
	•	Odd-indexed nodes.
	•	Even-indexed nodes.
	2.	Use two pointers: odd and even.
	3.	Traverse while connecting odds to odds and evens to evens.
	4.	Finally, connect the end of the odd list to the head of the even list.

Time Complexity: O(N)

Space Complexity: O(1) (no extra space)

Pros:
	•	In-place.
	•	Maintains node order and structure.

Cons:
	•	Slightly more pointer manipulation logic.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

# ===== User Input =====
arr = list(map(int, input("Enter linked list elements (space-separated): ").split()))
head = build_linked_list(arr)

# ===== Solve =====
solution = Solution()
new_head = solution.oddEvenList(head)

# ===== Output =====
print("Reordered Linked List (Odd followed by Even indices):")
print_linked_list(new_head)