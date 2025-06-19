def fibu(n):
    if n == 0 or n == 1:
        return n
    return fibu(n - 1) + fibu(n - 2)


class Solution:
    def fib(self, n: int) -> int:
        return fibu(n)
slv = Solution()
n = 30
print(slv.fib(n))
