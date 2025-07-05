"""
Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
"""


class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
arr = list(map(int,input("Enter space-separate integer: ").split()))
slv = Solution()
print(slv.arraySortedOrNot(arr))
