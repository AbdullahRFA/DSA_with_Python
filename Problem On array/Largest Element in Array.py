"""
Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
"""
class Solution:
    def largest(self, arr):
        # code here
        """
        arr.sort()
        return arr[-1]
        :param arr:
        :return:
        """
        le = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>le:
                le = arr[i]
        return le

arr = list(map(int, input("Enter space-separated integers: ").split()))
slv = Solution()
print("Largest element: ",slv.largest(arr))