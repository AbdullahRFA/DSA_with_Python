"""
Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

Example 1:

Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is
retained, rest nodes with value = 1 are deleted.
Example 2:

Input:
n = 7
1<->2<->2<->3<->3<->4<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of nodes with values 2,3 and 4 are
retained, rest repeating nodes are deleted.
Your Task:
You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list.  Your function should return a pointer to a linked list with no duplicate element.

Constraint:
1 <= n <= 105
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)


"""

# Back-end complete function Template for Python 3

'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
"""

⸻

Problem

Given a sorted doubly linked list, remove duplicate nodes so that only unique elements remain, while keeping the list linked properly in both directions.

⸻

Your approach (pointer manipulation method)

Idea
	1.	Traverse the list using a curr pointer.
	2.	For each node:
	•	If it’s the head node (curr.prev == None), move to the next — nothing to compare yet.
	•	If curr.data equals curr.prev.data:
	    •	If the duplicate is at the start of the list (curr.data == head.data):
	    •	Make curr the new head by setting head = curr and breaking the link to the old head.
	•	If the duplicate is in the middle:
	    •	Skip over the previous duplicate node by rewiring:
	    •	curr.prev.prev.next = curr
	    •	curr.prev = curr.prev.prev
	•	Else: simply move forward.

⸻

Key Operations
	•	Skipping duplicates by adjusting .next and .prev pointers so that the duplicate node is no longer linked.
	•	Updating the head when duplicates occur at the beginning.
	•	Ensuring bidirectional links remain consistent.

⸻

Why it works
	•	The list is sorted → duplicates will always be adjacent.
	•	By checking curr.data == curr.prev.data, you detect duplicates in one step.
	•	Pointer rewiring removes the unwanted node without extra space.

⸻

Time & Space Complexity
	•	Time Complexity: O(n) → one pass over the list.
	•	Space Complexity: O(1) → no extra memory used.

⸻

Caveats
	•	Need to check head is not None before accessing head.data to avoid AttributeError.
	•	Must carefully handle the case when removing duplicates at the head so head always points to a valid node.
	•	If all nodes are duplicates, you must handle the case where the list becomes empty.

⸻

"""

class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list

        # if not head or not head.next:
        #     return head

        # curr = head

        # while curr.next:
        #     if curr.data == curr.next.data:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # return head

        curr = head

        while curr:
            # if curr is the first element then pass
            if curr.prev == None:
                curr = curr.next

            elif curr.data == curr.prev.data and curr.data == head.data:
                curr.prev = None
                head = curr
            elif curr.data == curr.prev.data:
                curr.prev.prev.next = curr
                curr.prev = curr.prev.prev
            else:
                curr = curr.next
        return head




