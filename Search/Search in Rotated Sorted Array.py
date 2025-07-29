"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # LEFT HALF is sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # RIGHT HALF is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

slv = Solution()
# nums = [4,5,6,7,0,1,2]
nums = [3,1]
target = 1
print(slv.search(nums,target))

"""
⸻

🔍 Problem Summary

You’re given:
	•	A rotated sorted array (no duplicates).
	•	A target value.

You need to:
	•	Return the index of target if it exists, otherwise -1.

⸻

💡 Key Idea (Concept)

Even though the array is rotated, one half is always sorted.

🔁 Rotated Sorted Array Example:

Original:        [0, 1, 2, 4, 5, 6, 7]
Rotated:         [4, 5, 6, 7, 0, 1, 2]
Index:            0  1  2  3  4  5  6

🧠 Observation:

In any iteration:
	•	Either left to mid is sorted, or
	•	mid to right is sorted

Use that to decide which half to search.


⚙️ Step-by-Step Technique:

Step 1: Initialize

left = 0
right = len(nums) - 1

Step 2: Binary Search Loop
	•	While left <= right:
	•	Compute mid
	•	If nums[mid] == target: return mid

Step 3: Determine which half is sorted
	•	If nums[mid] >= nums[left] → left half is sorted
	•	Check if target lies between nums[left] and nums[mid]
	•	If yes, go left (right = mid - 1)
	•	Else, go right (left = mid + 1)
	•	Else → right half is sorted
	•	Check if target lies between nums[mid] and nums[right]
	•	If yes, go right
	•	Else, go left

⸻

🔍 Example: nums = [3, 1], target = 1

Iteration 1:
	•	left = 0, right = 1
	•	mid = 0 → nums[mid] = 3
	•	nums[mid] >= nums[left] → left half is sorted
	•	target = 1 is not between 3 and 3 → go right (left = mid + 1 = 1)

Iteration 2:
	•	left = 1, right = 1
	•	mid = 1 → nums[mid] = 1 → 🎯 Found! Return 1

⸻

🧠 Time and Space Complexity

Aspect	Value
Time	O(log n)
Space	O(1)


⸻

"""