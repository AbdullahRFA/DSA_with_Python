class Solution:
    def preFixToPostFix(self, s):
        stack = []

        # Remove spaces
        s = s.replace(" ", "")
        s = s[::-1]

        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                if len(stack) < 2:
                    return "Invalid Expression"

                op1 = stack.pop()
                op2 = stack.pop()

                stack.append(op1 + op2 + char)

        if len(stack) != 1:
            return "Invalid Expression"

        return stack[0]


slv = Solution()
inputValue = input("Enter the prefix expression: ")
print(inputValue)
print(slv.preFixToPostFix(inputValue))
# /-ab*+def