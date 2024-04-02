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
    stack=[]
    for a in A:
        if a=='(' or a=="[" or a=="{":
            stack.append(a)
        else:
            if len(stack)==0:
                return 0
            elif (stack[-1] == "(" and a==")") or (stack[-1] == "[" and a=="]") or (stack[-1] == "{" and a=="}"):
                stack.pop()
            else:
                return 0
            
        if len(stack)!=0:
            return 0
        else:
            return 1

s="()([])"
x=isValid(s)
print(x)

