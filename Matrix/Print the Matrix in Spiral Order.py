"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = top = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

# ========== User Input Section ==========

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix row by row (space-separated):")
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Invalid number of elements. Please enter", cols, "integers.")
        exit()
    matrix.append(row)

# ========== Run the Solution ==========

slv = Solution()
spiral = slv.spiralOrder(matrix)
print("Spiral Order:", spiral)

"""
🌀 Problem:

Given a 2D matrix, return all elements of the matrix in spiral order.

⸻

✅ Goal:

Traverse the matrix in layers:
	•	First top row
	•	Then rightmost column
	•	Then bottom row (in reverse)
	•	Then leftmost column (in reverse)
Repeat this by shrinking the boundaries until all elements are visited.

⸻

🔍 Step-by-Step Solution Technique:

Step 1: Initialize four pointers

        top = 0
        bottom = number of rows - 1
        left = 0
        right = number of columns - 1

These pointers help us keep track of the current layer/boundaries.

⸻

Step 2: Traverse the matrix layer by layer

While top <= bottom and left <= right:
	1.	Traverse from Left to Right (→) on the top row:
        •	Append matrix[top][i] from i = left to right
        •	Then move top += 1
	2.	Traverse from Top to Bottom (↓) on the rightmost column:
        •	Append matrix[i][right] from i = top to bottom
        •	Then move right -= 1
	3.	If top <= bottom, Traverse from Right to Left (←) on the bottom row:
        •	Append matrix[bottom][i] from i = right to left (in reverse)
        •	Then move bottom -= 1
	4.	If left <= right, Traverse from Bottom to Top (↑) on the leftmost column:
        •	Append matrix[i][left] from i = bottom to top (in reverse)
        •	Then move left += 1

Repeat until all elements are collected.

⸻

📦 Example:

For:

        [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
        ]

The spiral order is:

[1, 2, 3, 6, 9, 8, 7, 4, 5]


⸻

⏱️ Time & Space Complexity:

Aspect	Complexity
Time	O(m * n) where m = rows, n = columns
Space	O(1) extra (not counting result list)


⸻

"""