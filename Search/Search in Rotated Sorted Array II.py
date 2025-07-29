"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates: skip both ends
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# -------- User Input --------
nums = list(map(int, input("Enter the array (space-separated): ").split()))
target = int(input("Enter the target number: "))

sol = Solution()
result = sol.search(nums, target)
print("Target found?" , result)

"""

✅ Solution Technique: (for searching in Rotated Sorted Array with Duplicates)
	•	🔁 Binary Search Framework:
	•	Use the standard binary search loop while left <= right.
	•	🎯 Check for Direct Hit:
	•	If nums[mid] == target: return True.
	•	🌀 Handle Duplicates:
	•	If nums[left] == nums[mid] == nums[right]: increment left, decrement right to skip duplicates.
        (This breaks the sorted property, so we cautiously shrink the range.)
	•	🔄 Determine Sorted Side:
	•	If nums[left] <= nums[mid], then left half is sorted.
	•	Check if target is in this range: nums[left] <= target < nums[mid].
	•	Else, right half is sorted.
	•	Check if target is in this range: nums[mid] < target <= nums[right].
	•	🔁 Adjust left or right accordingly to search the next half.
	•	❌ If loop ends without a match: return False.

⸻

"""

