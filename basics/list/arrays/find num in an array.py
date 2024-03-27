'''FInd missing number in an array(using summation and xor operation)'''

#array 124567 here 3 is missing

#SUMMATION METHOD
'''the missing number we can find out sum of n natural numbers like here it is (1 to 7) using n*(n+1)/2
here we get 28, and sum of array is 25 therefore missing number is 28-25=3
'''
#array
a=[1,2,4,5,6,7]


def get_missing_summ(a):
    n=a[-1]
    summ=0
    total=n*(n+1)//2
    summ=sum(a)
    print(total-summ)

#get_missing_summ(a)


#Xor Method remember the xor table 
'''xor of (1 to n) natural numbers here n=7
n= 1 xor 2xor 3xor 4xor 5xor 6xor 7
             xor
array= 1 xor 2xor 4xor 5xor 6xor 7

will get 0xor 3 so 3 is the ans
'''
def get_missing_xor(a):
    n=len(a)
    xor_a=a[0] #index 1
    for index in range(1,n): #index 2 to last
        xor_a=xor_a^a[index] #1^2^3^4^5^7
    
    x2=0
    for index in range(1,n+2):
        x2=x2^index

    print(x2^xor_a)

get_missing_xor(a)    




