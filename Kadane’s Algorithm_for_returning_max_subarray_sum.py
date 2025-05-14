"""
Kadane’s Algorithm is one of the most famous and efficient algorithms in computer science for solving the “Maximum Subarray Sum” problem.

⸻

✅ Problem Statement

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.

⸻

🔍 Real Example

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.



⸻

🧠 Concept Behind Kadane’s Algorithm

Instead of checking all possible subarrays (which takes O(n²)), Kadane’s Algorithm smartly scans the array from left to right and keeps track of:
	•	current_sum: The maximum sum ending at the current position
	•	max_sum: The maximum seen so far

Step-by-Step:
	1.	Initialize:
	•	max_sum = current_sum = nums[0]
	2.	Loop through the array from index 1 to n-1:
	•	Update current_sum:

current_sum = max(nums[i], current_sum + nums[i])

Either:
	•	Start a new subarray at nums[i]
	•	Or extend the existing one

	•	Update max_sum:

max_sum = max(max_sum, current_sum)
⸻

🔢 Example Trace (Step-by-step)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Start:
current_sum = max_sum = -2

Index 1: 1
current_sum = max(1, -2+1) = 1
max_sum = max(-2, 1) = 1

Index 2: -3
current_sum = max(-3, 1 + (-3)) = -2
max_sum = 1

Index 3: 4
current_sum = max(4, -2+4) = 4
max_sum = max(1, 4) = 4

Index 4: -1
current_sum = max(-1, 4 + (-1)) = 3
max_sum = 4

Index 5: 2
current_sum = max(2, 3+2) = 5
max_sum = 5

Index 6: 1
current_sum = max(1, 5+1) = 6
max_sum = 6 ✅

Index 7: -5
current_sum = max(-5, 6+(-5)) = 1
max_sum = 6

Index 8: 4
current_sum = max(4, 1+4) = 5
max_sum = 6

Final max_sum = 6

⸻

⏱️ Time and Space Complexity
	•	Time Complexity: O(n) — one pass through the array
	•	Space Complexity: O(1) — only a few variables used

⸻

🧠 Summary

Concept	Description
Type	Dynamic Programming / Greedy
Goal	Max sum of contiguous subarray
Approach	Scan with running sum, reset if needed
Complexity	O(n) time, O(1) space



⸻

Would you like to see Kadane’s Algorithm for returning the subarray itself or use it on 2D arrays too?
"""
def kadane_algo(arr):
    max_sum = current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum+arr[i])
        max_sum = max(max_sum,current_sum)
    return max_sum

arr= [2, 3, -8, 7, -1, 2, 3]
print(kadane_algo(arr))