class Solution:
    def postFixToInfix(self,s):
        stack = []

        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                newExpression = f"({operand1}{char}{operand2})"
                stack.append(newExpression)
        return  stack[-1]

slv = Solution()
inputValue = input("Enter the postfix expression: ")
print(inputValue)
print(slv.postFixToInfix(inputValue))

# ab-de+f*/