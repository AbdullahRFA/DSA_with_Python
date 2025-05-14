"""

"""
"""

✅ Goal

Given an array of integers, find the maximum sum subarray (contiguous) and return both the sum and the subarray itself.

⸻

✅ Step-by-step Technique

⸻

Step 1: Initialize Tracking Variables

max_sum = current_sum = arr[0]
start = end = temp_start = 0

	•	max_sum: stores the best (maximum) sum found so far.
	•	current_sum: running total of the current subarray.
	•	start and end: track the indices of the best subarray.
	•	temp_start: marks the start of the current candidate subarray.

⸻

Step 2: Traverse the Array from Index 1

for i in range(1, len(arr)):

Start from index 1 (since arr[0] is already considered), and iterate through the array.

⸻

Step 3: Decide Whether to Start a New Subarray or Extend Current One

if arr[i] > arr[i] + current_sum:
    temp_start = i
    current_sum = arr[i]
else:
    current_sum += arr[i]

	•	If adding arr[i] to the current sum makes it worse, start a new subarray at i.
	•	Else, extend the current subarray to include arr[i].

This step ensures that we only keep subarrays that are profitable.

⸻

Step 4: Update Best Sum If Current Is Better

if max_sum < current_sum:
    max_sum = current_sum
    start = temp_start
    end = i

	•	If the current sum is better than the max seen so far:
	•	Update max_sum.
	•	Record the start and end positions for the best subarray.

⸻

Step 5: Return the Result

return max_sum, arr[start:end+1]

	•	Return the maximum sum and the actual subarray using slicing.

⸻

✅ Example Walkthrough

Given:

arr = [2, 3, -8, 7, -1, 2, 3]

	•	Starts with current_sum = max_sum = 2
	•	Iterates through and updates:
	•	At index 1 → adds 3, subarray becomes [2, 3], sum = 5
	•	At index 2 → adds -8, sum becomes -3
	•	At index 3 → 7 > -3 + 7, so start new subarray at index 3
	•	Continue adding -1, 2, 3
	•	Final subarray with max sum: [7, -1, 2, 3] = 11

⸻

✅ Output

11 [7, -1, 2, 3]



⸻

⏱️ Time & Space Complexity
	•	Time: O(n) → one pass through array.
	•	Space: O(1) → constant extra space (excluding the result).

⸻

Let me know if you’d like a visual trace or explanation using diagrams.
"""

def kadane_algo(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1,len(arr)):
        if arr[i] > arr[i]+current_sum:
            temp_start = i
            current_sum = arr[i]
        else:
            current_sum += arr[i]

        if max_sum < current_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum, arr[start:end+1]

# arr= [2, 3, -8, 7, -1, 2, 3]
arr = [1, 2, 3, 7, 5]
result = kadane_algo(arr)
print(result[0], result[1])