"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

"""

"""
✅ Solution Technique (Balanced Parentheses using Backtracking)
	•	Problem restatement:
Generate all possible balanced parentheses strings of length 2 * n.

⸻

🔹 Key Idea
	•	A balanced parentheses string must always satisfy:
        1.	Never more ')' than '(' at any point.
        2.	Exactly n '(' and n ')' total.
	•	To track balance:
	    •	total = current difference = open count - close count.
        •	If total ever becomes negative → invalid.
        •	If total ever exceeds n → invalid.

⸻

🔹 Recursive Backtracking Steps
	1.	Base Case:
	    •	If we filled all positions (idx == len(bracket))
             → add to result only if total == 0 (balanced).
	2.	Recursive Choices:
        •	Place '(':
        •	Increase total (Sum = total + 1).
        •	Recurse to next position.
        •	Place ')':
        •	Decrease total (Sum = total - 1).
        •	Recurse to next position.
	3.	Pruning (early stopping):
        •	If total > n → too many '(', stop.
        •	If total < 0 → too many ')', stop.

⸻

🔹 Why it works
	•	The recursion explores all possible placements of '(' and ')'.
	•	Pruning ensures only valid partial strings are extended.
	•	At the end, only balanced parentheses strings remain in result.

⸻

🔹 Example Walkthrough (n = 3)
	•	Start: idx=0, total=0
	•	Place '(' → total=1 → continue
	•	Place another '(' → total=2 → continue
	•	Place ')' → total=1 → continue
	•	Eventually: "((()))", "(()())", "(())()", "()(())", "()()()".

⸻

"""
from  typing import  List
class Solution:
    def Solve(self,idx, total,n, bracket, result):
        if idx>= len(bracket):
            if total == 0:
                result.append(''.join(bracket))
            return
        elif total > len(bracket)//2:
            return
        elif total < 0:
            return

        bracket[idx] = '('
        Sum = total + 1
        self.Solve(idx+1, Sum,n, bracket, result)
        bracket[idx] = ")"
        Sum = total - 1
        self.Solve(idx+1, Sum,n, bracket, result)


    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        bracket = [''] * (n * 2)
        self.Solve(0,0,n,bracket,result)
        return  result

slv = Solution()
n = int(input("Enter the value of 'n' : "))

print(slv.generateParenthesis(n))