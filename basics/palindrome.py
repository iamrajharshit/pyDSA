s1="hello"
s2="NMAMIT"
s3="aaaalllloooooooollllaaaa"

def palin(s):
    if s==s[::-1]:
        return "Palin"
    else:
        return "Non Palin"
    
def pal(s):
    s_len=len(s)
    s2=""
    for i in range(0,s_len):
        s2+=s[s_len-1-i]
    if s==s2:
        print("palindrome") 
    else:
        print("non palin")       


a1=pal(s1)
#print(a1)
a2=pal(s2)
#print(a2)
a3=pal(s3)       
#print(a3)
    
