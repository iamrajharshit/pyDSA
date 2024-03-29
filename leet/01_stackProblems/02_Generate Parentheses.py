'''
#leetcode 22
Given n pairs of parentheses, write a function to generate all combinations of well-formed 
parentheses.

example:
input: n=3
output: ["((()))","(()())","(())()","()(())","()()()"]

input: n=1
output: ["()"]
'''
"""
- We only start with open paren.
- open paren <=n before we close #base case (n open, n close)
- we should hane open and close count, when open == close, we cant close
- close<open; we are allowed to have an open paren.

"""

#only add open paren. if open <n
#only add a closing paren. if closed < open
#valid IIF open == closed == n

def genParen(n):
    #recussion
    stack=[] #holds paren
    result=[] #valid comb

    def backtrack(openN, closedN):
        #base case
        if openN==closedN==n:
            result.append("".join(stack)) #combination added to the result
            return
        if openN<n:
            stack.append("(")
            backtrack(openN+1,closedN)
            #after that backtracking returns we update the stack,as we have a single stack variable
            #we are not passing the stack into every single call, as its a global variable, so every time we are
            #done with backtracking, we pop last chr that we just added to the stack.
            stack.pop()

        if closedN<openN:
            stack.append(")")
            backtrack(openN,closedN+1)
            # popping the char that we just added.
            stack.pop()

    backtrack(0,0) #stack is empty init.

    return result

x=genParen(2)
print(x)