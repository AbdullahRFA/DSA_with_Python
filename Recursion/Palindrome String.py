#User function Template for python3
def fun(s,l,r):
    if l>r:
        return True
    if s[l] != s[r]:
        return False
    return fun(s,l+1,r-1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
# 		return s == s[::-1]
        return fun(s,0,len(s)-1)
slv = Solution()
s = "wbklpwm"
print(slv.isPalindrome(s))