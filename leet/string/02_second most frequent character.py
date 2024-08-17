def sec2(str):

    count=[0]*256 #chr init

    for i in range(len(str)):
        count[ord(str[i])]+=1 #using asci valued index to count freq

    f,s=0,0

    for i in range(len(count)):
        if count[i]>count[f]:
            s=f
            f=i
    
        elif count[i]>count[s] and count[i]<count[f]:
            s=i

    return chr(s)

print(sec2("aaacccccccdd"))


