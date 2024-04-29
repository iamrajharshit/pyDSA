#Given an array nums, write a function to move all 0's 
# to the end of it while maintaining the relative order of the 
#non-zero elements.

#in-place
#sol in O(n)

#if zero is countered hold it and swap with a number
# pointer1 for loop i=0 to end
# pointer2 prev=0
a=[1,0,3,0,4,0,5]
def sol(a):
    pre_indx=0 #p2 and i=p1
    for i in range(0,len(a)):
        if a[i]!=0:
            hold=a[pre_indx]
            a[pre_indx]=a[i]
            a[i]=hold
            pre_indx=pre_indx+1

print(a)
x=sol(a)
print(a)            

# 2 d sol
num=[1,2,0,5,0,15,0]

def move_zeros(num):
    pos=0
    for j in range(len(num)):
        if num[j]!=0:
            num[pos],num[j]=num[j],num[pos]
            pos=pos+1
    return num