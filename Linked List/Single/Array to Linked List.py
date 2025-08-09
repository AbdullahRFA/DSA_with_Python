"""
Given an array of integer arr. Your task is to construct the linked list from arr & return the head of the linked list.

Examples:

Input: arr = [1, 2, 3, 4, 5]
Output: LinkedList: 1->2->3->4->5
Explanation: Linked list for the given array will be

Input: arr = [2, 4, 6, 7, 5, 1, 0]
Output: LinkedList: 2->4->6->7->5->1->0
Explanation: Linked list for the given array will be

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 106
"""


# User function Template for python3


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class SingleLinkLIst:
    # def __init__(self):
    #     self.head = None
    #
    # def append(self, val):
    #     new_node = Node(val)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #
    #     current = self.head
    #     while current.next is not None:
    #         current = current.next
    #     current.next = new_node

    def traversal(self,head):
        current = head

        while current :
            print(current.data,end=" ")
            current = current.next
        print()



class Solution:
    def constructLL(self, arr):
        # code here
        # sll = SingleLinkLIst()
        head = None
        tail = None
        for x in arr:
            new_node = Node(x)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return head
slv = Solution()
arr = [2, 4, 6, 7, 5, 1, 0]
head = slv.constructLL(arr)
sll = SingleLinkLIst()
sll.traversal(head)
