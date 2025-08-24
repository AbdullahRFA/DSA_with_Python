"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
"""

⸻

✅ Problem Restatement
	•	Given a list of distinct positive integers (candidates) and a target,
        find all unique combinations of numbers where the chosen numbers sum up to target.
	•	You can use the same number unlimited times.

⸻

🔹 Key Idea
	•	Use backtracking (DFS recursion) to explore all possible choices.
	•	At each step, you can either:
	    1.	Pick the current number again (since repetition allowed).
	    2.	Skip the current number and move to the next one.

⸻

🔹 Recursive Function Parameters
	•	idx → current index in candidates.
	•	total → running sum of the chosen numbers.
	•	subset → current combination being built.
	•	result → stores all valid combinations.

⸻

🔹 Base Cases
	1.	If total == target:
	    •	Found a valid combination → add a copy of subset to result.
	2.	If total > target:
	    •	Invalid path (sum exceeded target) → backtrack (stop recursion).
	3.	If idx >= len(candidates):
	    •	Reached beyond available numbers → stop recursion.

⸻

🔹 Recursive Choices
	•	Include (pick) candidates[idx]:
        •	Add it to subset.
        •	Recurse with same idx (since repetition allowed).
        •	Increase total by candidates[idx].
	•	Exclude (not pick) candidates[idx]:
        •	Remove last element from subset.
        •	Recurse with idx+1.
        •	Keep total unchanged.

⸻

🔹 Why It Works
	•	The recursion tree explores all possible inclusion/exclusion paths.
	•	By allowing “pick same index again”, we handle repeated usage.
	•	By moving to idx+1, we ensure combinations are built without duplicates.

⸻

🔹 Example Walkthrough (candidates = [2,3,6,7], target=7)
	1.	Start with idx=0, total=0, subset=[].
	2.	Pick 2: → subset=[2], total=2.
        •	Pick 2 again: → [2,2], total=4.
        •	Pick 2 again: → [2,2,2], total=6.
        •	Pick 2 again: → [2,2,2,2], total=8 → stop (exceeded).
        •	Backtrack → try other paths.
	3.	Later, path [2,2,3] → valid (sum=7).
	4.	Path [7] → valid (sum=7).
	5.	Result = [[2,2,3], [7]].

⸻
"""
from typing import List
class Solution:
    def Solve(self, idx, total, candidates, target, subset, result):

        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        elif idx >= len(candidates):
            return

        Sum = total + candidates[idx]
        subset.append(candidates[idx])
        self.Solve(idx, Sum, candidates, target, subset, result)
        Sum = total
        subset.pop()
        self.Solve(idx+1, Sum, candidates, target, subset, result)



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        self.Solve(0,0,candidates,target,subset,result)
        return result



slv = Solution()
candidates = [2,3,6,7]
target = 7
print(slv.combinationSum(candidates,target))