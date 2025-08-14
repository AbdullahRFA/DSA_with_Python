"""
Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.



Example 1:

Input:
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs
(1, 6) and (2,5) with sum 7.


Example 2:

Input:
1 <-> 5 <-> 6
target = 6
Output: (1,5)
Explanation: We can see that there is one pairs  (1, 5) with sum 6.



Your Task:
You don't need to read input or print anything. Your task is to complete the function findPairsWithGivenSum() which takes head node of the doubly linked list and an integer target as input parameter and returns an array of pairs. If there is no such pair return empty array.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 105
1 <= target <= 105


"""

from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

from typing import Optional

from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        # code here

        # Brute forece solution
        # res = []
        # temp1 = head

        # while temp1:
        #     temp2=temp1
        #     while temp2:
        #         if temp1.data + temp2.data == target:
        #             res.append([temp1.data, temp2.data])
        #         temp2 = temp2.next
        #     temp1 = temp1.next
        # return res

        # better solution

        # seen = set()
        # res = set()
        # curr = head

        # while curr:
        #     complement = target - curr.data
        #     if complement in seen:
        #         # store pair in sorted order to avoid (4,1) vs (1,4)
        #         pair = tuple(sorted((complement, curr.data)))
        #         res.add(pair)
        #     seen.add(curr.data)
        #     curr = curr.next

        # # convert set of tuples to sorted list of lists
        # return [list(pair) for pair in sorted(res)]

        # Optimal Solution

        res = []
        left = right = head

        while right.next:
            right = right.next

        while left and right and left.data < right.data:
            total = right.data + left.data
            if total == target:
                res.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif total > target:
                right = right.prev
            else:
                left = left.next
        return res










