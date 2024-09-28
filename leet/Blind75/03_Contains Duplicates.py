'''
Print  true if cantains duplicates else false 
'''

arr=[1,2,3,1]
# output True

def TF4arr(arr):
    mapx={}
    for i in range(len(arr)):
        mapx[arr[i]]=mapx.get(arr[i],0)+1
    #print(mapx)
    # if 2 in mapx.values():
    #     return True
    # return False
    for k,v in mapx.items():
        if v>1:
            return True
        return False


# print(TF4arr(arr))

print(TF4arr(arr))

##############################################

def dup_num(arr):
    hashset=set()
    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)
        return False