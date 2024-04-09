'''Given an array of integers, return indices of the two numbers such that they add up
to a specific target.
You may assume that each input would have exactly one solution and you may not use the same element twice.

//Example:
given nums=[2,7,11,15] target=9

here 2+7=9
return [0,1]
'''

#this is our list
n=[2,7,11,15]
# the target 
target=9

#our function to find sum of two
def twoSUM(n,target):
    Hmap={} #hash map or a dict in py which contains key:value
    #here key is list element with value its index.
    for i,n in enumerate(n):
        diff=target-n   #if the diff between the target and the curr number is present in the Hmap
        if diff in Hmap:
            return [Hmap[diff],i]
        Hmap[n] =i #key (n) storing its value which is index(i)

    return

print(twoSUM(n,target))