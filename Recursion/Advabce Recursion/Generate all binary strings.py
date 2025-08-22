"""
Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1.

Example 1:

Input:
N = 3
Output:
000 , 001 , 010 , 100 , 101
Explanation:
None of the above strings contain consecutive 1s. "110" is not an answer as it has '1's occuring consecutively.
Your Task:

You don't need to read input or print anything. Your task is to complete the function generateBinaryStrings() which takes an integer N as input and returns a list of all valid binary strings in lexicographically increasing order.

Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 20


"""

"""

Enter length of binary strings: 3
Generated Binary Strings (no consecutive 1's):
000
001
010
100
101


⸻

📝 Solution Technique (Step by Step)
	•	Goal: Generate all binary strings of length n such that no two consecutive 1s appear.

	1.	Backtracking Setup
        Use recursion to build the string position by position. Keep an array number of size n.
	2.	Flag for consecutive check
        Maintain a flag variable:
        •	True → allowed to place 1 at this index.
        •	False → cannot place 1 here (because previous index already has 1).
	3.	Choices at each index
        •	Always try placing '0' (safe option, no restriction).
        •	If flag is True, also try placing '1'. After placing 1, set flag to False for the next index.
	4.	Base case
        When index == n, store the string (join the list of characters into "0101...").
	5.	Backtracking
        After exploring one branch, reset the current position (number[index] = "0") to maintain correctness.
	6.	Result
        Collect all valid strings in a list and return them.

⸻


"""
# User function Template for python3

class Solution:
    def solve(self, index, flag, number, result):
        # Base case: if we reached the end, save the string
        if index >= len(number):
            result.append(''.join(number))
            return

        # Always put '0'
        number[index] = "0"
        self.solve(index + 1, True, number, result)

        # Only put '1' if the previous was not '1'
        if flag:
            number[index] = "1"
            self.solve(index + 1, False, number, result)
            number[index] = "0"  # reset for backtracking

    def generateBinaryStrings(self, n):
        number = ["0"] * n
        result = []
        self.solve(0, True, number, result)
        return result


# -------------------------
# Driver Code for User Input
# -------------------------
if __name__ == "__main__":
    n = int(input("Enter length of binary strings: "))
    sol = Solution()
    ans = sol.generateBinaryStrings(n)
    print("Generated Binary Strings (no consecutive 1's):")
    for s in ans:
        print(s)