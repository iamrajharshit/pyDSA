'''
#leetcode 20
Given a string s containing just the char '(',')','{','}','[',']'
determine if the input string is valid or not.

Input="()"
Output=True

Input=")("
Output=False

stack: memory O(n)
       time O(n)
'''
def isValid(s):
    #a stack like list
    stack=[]
    # dict with keys as closing bracket and values as opening bracket
    chrMap={")":"(","}":"{","]":"["}

    #for every char in the string
    for chr in s:
        # if char is in the dict (keys will match )}]) if its there
        if chr in chrMap:
            #print(chr,"-->",chrMap[chr])
            if stack and stack[-1]==chrMap[chr]:# if stack not empty and stack last ele matches with the value of the dict 
                #print("last ele",stack[-1],"-->",chrMap[chr])
                #print("in stack",chrMap[chr],"pop")
                stack.pop() #pop the ele
                #print("Stack",stack)
            else:
                return False #if stack empty return False
        else:
            #print("append",chr)
            stack.append(chr) #append the ele to the stack
            #print("stack",stack)

    return True if not stack else False #if stack empty return True else return False


def isvalid(A):
    # Initialize an empty stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the input string A
    for a in A:
        # If the character is an opening bracket, push it onto the stack
        if a == '(' or a == "[" or a == "{":
            stack.append(a)
        else:
            # If the character is a closing bracket and the stack is empty,
            # it means there is no corresponding opening bracket, so return 0 (invalid)
            if len(stack) == 0:
                return 0
            # Check if the top of the stack has the corresponding opening bracket
            elif (stack[-1] == "(" and a == ")") or(stack[-1] == "[" and a == "]") or (stack[-1] == "{" and a == "}"):
                # If matched, remove the opening bracket from the stack
                stack.pop()
            else:
                # If there is a mismatch, return 0 (invalid)
                return 0
    
    # After processing all characters, check if the stack is empty
    # If the stack is not empty, it means there are unmatched opening brackets
    if len(stack) != 0:
        return 0
    else:
        # If the stack is empty, it means all brackets are balanced
        return 1

# Test the function with a sample input
s = "()([])"
x = isvalid(s)  # Call the function with the test string
print(x)  # Output the result: 1 if valid, 0 if invalid


