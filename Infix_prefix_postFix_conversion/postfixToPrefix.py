class Solution:
    def postfixToPrefix(self, s):
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                nexExpre = f"{char}{operand1}{operand2}"
                stack.append(nexExpre)
        return  stack[-1]


slv = Solution()
inputValue = input("Enter the postfix expression: ")
print(inputValue)
print(slv.postfixToPrefix(inputValue))
