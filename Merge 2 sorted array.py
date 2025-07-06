"""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2.
"""


# User function Template for python3

class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        # code here
        # a = set(a)
        # b = set(b)

        # c = a.union(b)
        # c = sorted(c)
        # return c

        i, j = 0, 0
        n, m = len(a), len(b)
        seen = set()
        res = []
        while i < n and j < m:
            if a[i] <= b[j]:
                if a[i] not in seen:
                    res.append(a[i])
                    seen.add(a[i])
                i += 1
            else:
                if b[j] not in seen:
                    res.append(b[j])
                    seen.add(b[j])
                j += 1
        if i < n:
            while i < n:
                if a[i] not in seen:
                    res.append(a[i])
                    seen.add(a[i])
                i += 1

        elif j < m:
            while j < m:
                if b[j] not in seen:
                    res.append(b[j])
                    seen.add(b[j])
                j += 1

        return res

slv = Solution()
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
print(slv.findUnion(a,b))





