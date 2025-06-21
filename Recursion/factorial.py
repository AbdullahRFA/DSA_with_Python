# def fun(n):
#     if n==1:
#         return 1
#     return n*fun(n-1)
# n = int(input("Enter a number to find factorial: "))
# print(fun(n))

# Optimized factorial using memoization
def fun(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = n * fun(n - 1, memo)
    return memo[n]

class Solution:
    def factorial(self, n):
        return fun(n)

# Driver Code for User Input
if __name__ == "__main__":
    n = int(input("Enter a number to find its factorial: "))
    ob = Solution()
    print(f"Factorial of {n} is:", ob.factorial(n))

