arr=[1,2,3,4]

res=[1]*len(arr)
# p=0
# n=len(arr)-1
for c in range(len(arr)):
    p=0
    n=len(arr)-1
    m=1
    if c==0:
        while(n>c):
            m=m*arr[n]
            n=n-1
        res[c]=m
    elif c==len(arr)-1:
        while(p<c):
            m=m*arr[p]
            p+=1
        res[c]=m
    # elif c>0 and c<=len(arr):
    while(p<c and n>c):
        m=m*arr[n]*arr[p]
        p+=1
        n-=1
    res[c]=m

# print(res)
######################OPTIMAL###########################################

pref= 1
sif= 1    
for i in range(len(arr)):
    res[i]=pref
    pref=pref*arr[i] #prev products

for i in range(len(arr)-1,-1,-1):
    res[i]=res[i]*sif
    sif=sif*arr[i] #suf products

print(res)