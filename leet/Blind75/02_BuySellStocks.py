'''
Design an algo. for max profit.
'''
arr=[7,1,5,3,6,4]
#output: 5

def maxProfit(arr):
    b=0
    s=1
    maxp=0

    while(s<len(arr)):
        if arr[b]>arr[s]:
            b=s
        maxp=max(maxp,arr[s]-arr[b])
        s=s+1
    return maxp