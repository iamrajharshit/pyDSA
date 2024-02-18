# 1342. Number of Steps to Reduce a Number to Zero
'''Through this problem, you will learn how to identify if a number is even or odd
 (hint, think about the modulo operator from the previous problem).
 For those who are looking for an added challenge,
 you can try solving this problem using bitwise operations.'''

def num_of_steps(num):
    steps=0
    while num>0:
        if num % 2==0:
            num/=2
        else:
            num-=1
        steps+=1
    return steps
        

a=num_of_steps(3)
print(a)

#time comp O(logn)    

'''Binary rep of integers, Bitwise shift operations,
Bitwise Logical operations and bitmasks'''


