'''
Product of array expect self.

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

'''

arr=[1,2,3,4]
# output= [24,12,8,6]

res=[1]*len(arr)

pre =1
for i in range(len(arr)):
    res[i]=pre
    pre*=arr[i]

post=1
for i in range(len(arr)-1,-1,-1):
    res[i]*=post
    post*=arr[i]

print(res)