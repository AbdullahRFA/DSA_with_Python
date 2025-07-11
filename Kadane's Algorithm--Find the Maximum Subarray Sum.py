
from typing import  List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Brute force solution
        """
        maxi = float("-inf")
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i,n):
                total += nums[j]
                maxi = max(maxi,total)
        return maxi
        """

#         Kadane's Algorithm
        total = 0
        maxi = float("-inf")
        for x in nums:
            total+=x
            maxi = max(total,maxi)
            if total < 0:
                total = 0
        return maxi



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
slv = Solution()
print(slv.maxSubArray(nums))