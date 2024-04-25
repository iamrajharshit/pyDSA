'''
https://www.youtube.com/watch?v=Y0lT9Fck7qI
You are climbing a staircase. It takes n steps ro reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?


#Example

Input: n=2
Output: 2

Explaination: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Input: n=3
Output: 3

Explaination: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 step
3. 2 step + 1 step
'''

'''
Tree
Solve with recursion 
basecase: steps == n return 1
basecase: steps > n return 0

Bottom Up Programming Aproach
Fibo
two var shifted n-1 times
'''


#code
def climbStar(n):
    one,two=1,1

    for i in range(n-1):
        temp=one
        one=one+two
        two=temp

    return one

print(climbStar(5))
