class Solution:
    def prefixToInfix(self, s):
        stack = []
        s = s[::-1]

        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()

                newExp = f"({operand1}{char}{operand2})"
                stack.append(newExp)
        return stack[-1]


slv = Solution()
inputValue = input("Enter the prefix expression: ")
print(inputValue)
print(slv.prefixToInfix(inputValue))

# *+pq-mn