arr=[1,3,4,5,6,7,8]

larg=arr[0]
sec=-1
for i in range(len(arr)):
    if arr[i]>larg:
        sec=larg
        larg=arr[i]

    if arr[i]>sec and arr[i]<larg:
        sec=arr[i]

print(sec)


    
    