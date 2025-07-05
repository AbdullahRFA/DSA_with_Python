"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k = k%n

        # nums[:]=nums[n-k:]+nums[:n-k]
        """
        🔹 How it works:
	•	nums[n-k:]: takes the last k elements
	•	nums[:n-k]: takes the first n-k elements
	•	Concatenates both, assigns back to nums using slice assignment
        """
        # for _ in range(k):
        #     temp = nums.pop()
        #     nums.insert(0,temp)
        """
        🔹 How it works:
	•	Pops last element and inserts it at the beginning, k times
        """

        def rotate(arr,l,r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        rotate(nums,n-k,n-1)
        rotate(nums,0,n-k-1)
        rotate(nums,0,n-1)
        """
        🔹 How it works:
            1.	Reverse last k elements
            2.	Reverse first n-k elements
            3.	Reverse the whole array
        """
slv= Solution()
nums = [1,2,3,4,5,6,7]
# nums=[1]
k = 3
# print(nums.pop())
# nums.insert(0,7)
slv.rotate(nums,k)
print(nums)