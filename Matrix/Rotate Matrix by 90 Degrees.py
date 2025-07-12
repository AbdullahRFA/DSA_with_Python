from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use extra space
        # n,m=len(matrix),len(matrix[0])
        # res=[[0 for _ in range(n)]for _ in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         res[j][m-1-i]=matrix[i][j]
        # for row in res:
        #     print(row)

        # in place solution
        """
        1. first transpose the mat
        2. second sort each row
         finally got 90 deg rotate mat
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # for row in matrix:
        #     print(row)
        for x in matrix:
            x.reverse()
        print()
        # for row in matrix:
        #     print(row)



n,m = map(int,input("Enter row and column: ").split())
matrix = []
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
for row in matrix:
    print(row)
print()
slv = Solution()
slv.rotate(matrix)
for row in matrix:
    print(row)
