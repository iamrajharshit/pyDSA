class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        for a in A:
            if a == '(' or a == '[' or a == '{':
                stack.append(a)
            else:
                if len(stack) == 0:
                    return 0
                elif (stack[-1] == '(' and a == ')') or (stack[-1] == '[' and a == ']') or (stack[-1] == '{' and a == '}'):
                    stack.pop()
                else:
                    return 0
        if len(stack) != 0:
            return 0
        return 1
