'''
Two Sum problem:
arr=[2,1,5,3]
targ=4
'''

# Logic: Looking for target minus the arr val if exsits in the dict.
arr=[2,1,5,3]
targ=4


def TwoSum(arr,targ):
    #hashmap
    mapx={}
    for i, v in enumerate(arr):
        if targ-v in mapx:
            return [arr[targ-v],i]
        else:
            mapx[v]=i


print(TwoSum(arr,targ))