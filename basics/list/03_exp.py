def balancing (exp):
    stack=[]

    for char in exp:
        if char in ['(',"{","["]:
            stack.append(char)

        else:
            if not stack:
                return False
            
            curr_char=stack.pop()
            if curr_char=='(':
                if char !=")":
                    return False
            if curr_char=='{':
                if char !="}":
                    return False
            if curr_char=='[':
                if char !="]":
                    return False 
    if stack:
        return False
    else:
        return True
    
exp="[]{}()"
x=balancing(exp)    
print(x)