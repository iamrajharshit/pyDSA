'''
Find missing num in an array (1 to n).

'''

arr=[1,5,2,4]
n=5
#simple approach
'''Matching with numbers in the given range 1 to n'''
def find_num1(n,arr):
    for i in range(1,n):
        if i in arr:
            continue
        else:
            return i

#Flag approach
'''Flag approach, using two loops if the number in the give range of loop,'''
def find_num2(arr):
    for i in range(len(arr)):
        f=0
        for j in range(len(arr)-1):
            if arr[j]==i:
                f=1
                break

    if f==0:
        return i
    


# hashmap approach

def find_num3(n,arr):
    hash={i:0 for i in range(1,n+1)}
    #print(hash)

    for j in range(len(arr)): #indx here is for the arr right
        #print(arr[j],j)
        hash[arr[j]]=1
        #print(hash)

    for j in range(1,n+1):
        if hash[j]==0:
            return j


#Bit appraoch using xor

def find_num4(n,arr):
    xor1=0
    xor2=0

    for i in range(1,n+1):
        xor1=xor1^i

    for j in range(0,len(arr)):
        xor2=xor2^arr[j]

    return xor1^xor2

#opt. Bit xor

def find_num5(n,arr):
    x1,x2=0,0
    for i in range(len(arr)):
        x2=x2^arr[i]
        x1=x1^(i+1)
    x1=x1^n
    return x1^x2

print(find_num5(n,arr))

print(find_num4(n,arr=[1,2,4,5]))
print(find_num3(n,arr))

print(find_num2(arr))

print(find_num1(n,arr))


