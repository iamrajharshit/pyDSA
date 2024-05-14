
s="Hello"

def isPAL(s):
    #start
    i=0
    #end
    j=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            j-=1
    return True
            
print(isPAL(s))            