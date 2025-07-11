"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
"""


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        # Brute force solution O(N^2)
        n = len(nums)
        max_cnt = 0
        for x in nums: # O(N)
            cnt = 1
            num = x
            while num+1 in nums: # O(N)
                cnt+=1
                num = num+1
            max_cnt = max(max_cnt,cnt)
        return max_cnt

        '''

        '''
        # Better solution
        
        last_element = float("-inf")
        nums.sort() # O(NlogN)
        max_cnt = 0
        cnt = 1
        for x in nums: # O(N)
            if abs(x-last_element)==1:
                cnt+=1
                last_element = x
                max_cnt = max(max_cnt, cnt)
            elif abs(x-last_element)==0:
                continue
            elif abs(x-last_element)>1:
                last_element=x
                cnt=1

        return max_cnt
        
        '''
        # Optimal solution
        nums = set(nums)
        longest = 0
        for x in nums:
            cnt = 1
            if x-1 not in nums:
                while x+1 in nums:
                    cnt+=1
                    x = x+1
            longest = max(longest,cnt)
        return  longest





nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]

slv = Solution()
print(slv.longestConsecutive(nums))

"""

✅ Problem Summary:

Given an unsorted list of integers, return the length of the longest consecutive sequence.
The goal is to do this in O(n) time.

⸻

1️⃣ Brute Force Solution

🔍 Approach:
	•	For each number x in the array:
	•	Check whether x+1, x+2, …, exist in the array.
	•	Count how long the sequence goes starting from x.

🧠 Logic:

for x in nums:
    count = 1
    while x + 1 in nums:
        x += 1
        count += 1
    max_count = max(max_count, count)

⏱️ Time Complexity:
	•	Outer loop: O(n)
	•	Inner loop (search in list): O(n) in worst case (because in takes O(n) in a list)
	•	Overall: O(n²)

🧠 Space Complexity:
	•	O(1) (no extra space except variables)

⸻

2️⃣ Better (Sorting-Based) Solution

🔍 Approach:
	•	Sort the array.
	•	Loop through the sorted array and count increasing consecutive elements.
	•	Handle duplicates by skipping them.

🧠 Logic:

nums.sort()
for x in nums:
    if x == last: continue
    elif x == last + 1: count += 1
    else: count = 1

⏱️ Time Complexity:
	•	Sorting: O(n log n)
	•	Traversal: O(n)
	•	Overall: O(n log n)

🧠 Space Complexity:
	•	Depends:
	•	O(1) for in-place sort
	•	O(n) if sort creates a new list

⸻

3️⃣ Optimal Solution (Using Set)

🔍 Approach:
	•	Convert nums to a set for O(1) lookup.
	•	Loop through each number, and only start counting if x - 1 is not in the set (i.e., start of a new sequence).
	•	Count the length of the sequence from x.

🧠 Logic:

nums_set = set(nums)
for x in nums_set:
    if x - 1 not in nums_set:
        count = 1
        while x + 1 in nums_set:
            x += 1
            count += 1

⏱️ Time Complexity:
	•	Converting to set: O(n)
	•	Traversal: O(n)
	•	Each element is visited at most once in the inner while loop.
	•	Overall: O(n) ✅

🧠 Space Complexity:
	•	Set to hold n elements → O(n)

⸻

✅ Final Comparison Table

Method	    Time Complexity	    Space Complexity	             Notes
Brute Force	    O(n²)	            O(1)	        Simple, but too slow for large input
Sorting Based	O(n log n)	      O(1) or O(n)	    Acceptable, but not optimal
Optimal (Set)	O(n)	            O(n)	        Best choice – Fast and efficient ✅


⸻

"""