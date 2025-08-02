"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.
"""


"""
We want to delete the middle node. If the list has only one node, return None.

Otherwise:
	•	Use a slow and fast pointer to find the middle.
	•	Keep a prev pointer to track the node before the slow node.
	•	When fast reaches the end, delete slow.
"""
from typing import Optional

# Step 1: Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 2: Solution class with deleteMiddle method
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None  # Only one node, return None

        fast = head
        slow = head
        previous = None

        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = previous.next.next
        return head

# Step 3: Helper to create linked list from list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Step 4: Helper to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' -> ' if current.next else '\n')
        current = current.next

# Step 5: Take user input and test
if __name__ == "__main__":
    nums = list(map(int, input("Enter space-separated list elements: ").split()))
    head = build_linked_list(nums)

    solution = Solution()
    updated_head = solution.deleteMiddle(head)

    print("Linked list after deleting middle node:")
    print_linked_list(updated_head)

