class Solution:
    def precedence(self, char):
        if char == '+' or char == '-':
            return 1
        elif char == '*' or char == '/':
            return 2
        elif char == '^':
            return 3
        return 0

    def infixToPostFix(self,s):
        stack = []
        result = []
        for char in s:
            if ('a'<= char <= 'z') or ('A'<= char <= 'Z') or ('0'<= char <='9'):
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ")":
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence((stack[-1]))>= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
        while stack:
            result.append(stack.pop())
        return "".join(result)




slv = Solution()
inputValue = input("Enter the infix expression: ")
print(inputValue)
print(slv.infixToPostFix(inputValue))