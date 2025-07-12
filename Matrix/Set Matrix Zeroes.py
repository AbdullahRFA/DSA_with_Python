"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""
"""

✅ Problem Statement:

Given a m x n matrix, if an element is 0, set its entire row and column to 0 in-place.

Example:

Input:
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]

Output:
matrix = [[1,0,1],
          [0,0,0],
          [1,0,1]]


⸻

✅ Your Code: Summary

Your code performs the following steps:

⸻

✅ Step-by-Step Solution Technique:

Step 1: Find all the positions where value is 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            dct[k] = [i, j]

	•	Traverse the entire matrix.
	•	Store the coordinates of all zero-valued cells in a dictionary dct.
	•	k is just a unique key for each zero position.

⸻

Step 2: For each zero position, update its row and column to zero

for x in dct.values():
    i = x[0]
    j = x[1]
    # set column to zero
    ...
    # set row to zero
    ...

	•	For each stored zero cell at (i, j), you:
	•	Set all elements in row i to 0.
	•	Set all elements in column j to 0.

⸻

✅ Approach Complexity:

Type	Complexity
Time	O(k * (m + n)) — k is number of zeros
Space	O(k)

"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        dct = {}
        k = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dct[k] = [i, j]
                    k += 1
        for x in dct.values():
            i, j = x
            # Set entire column j to 0
            for r in range(n):
                matrix[r][j] = 0
            # Set entire row i to 0
            for c in range(m):
                matrix[i][c] = 0

# ------- User Input --------
def take_input():
    print("Enter the number of rows and columns:")
    n, m = map(int, input().split())

    print("Enter the matrix row by row (space separated):")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix

# Input and processing
matrix = take_input()

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Apply setZeroes
slv = Solution()
slv.setZeroes(matrix)

print("\nMatrix after applying setZeroes:")
for row in matrix:
    print(row)