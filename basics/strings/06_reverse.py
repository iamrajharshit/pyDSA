# reverse a string
s1="APPLE"
# s2=s1[::-1]
# print(s2)


def rev(s1):
    s2=""
    s_len=len(s1)
    for i in range(0,s_len):
        s2+=s1[s_len-1-i]
    print(s2)

rev(s1)
    