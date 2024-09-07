arr=[1,1,2,3,4,5,6,7,8]

print(len(arr))
i=0
j=1
while(i<j and j<len(arr)):
    if arr[i]==arr[j]:
        del arr[j]
    else:
        i+=1
        j+=1
print(len(arr))
