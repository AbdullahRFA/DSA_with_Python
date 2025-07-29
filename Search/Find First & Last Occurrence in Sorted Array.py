from typing import List
def lowerBound(nums,target):
    left = 0
    right = len(nums) - 1
    lb = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            lb = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid-1
    return lb
def upperBound(nums,target):
    left = 0
    right = len(nums) - 1
    ub = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ub = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # ub = ub-1 if ub>1 else -1
    return ub
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = lowerBound(nums,target)
        last = upperBound(nums,target)

        return [first,last]



        # Brute force solution
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i
        # return [first,last]

slv = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(slv.searchRange(nums,target))
