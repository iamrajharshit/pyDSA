def twoSum(a,target):
    #start
    i=0
    #end
    j= len(a)-1

    while i<j:
        sm =a[i] + a[j]
        if target == sm:
            print(f"the numbers: {a[i]} and {a[j]}")
            print(f"{i} and {j} are the index values")
            return True
        elif sm < target:
            i+=1
        else: #sm>target
            j-=1
    return False

test_case=int(input())

for i in range(test_case):
    a=list(map(int,input().split()))
    #sort the list
    target=int(input())
    print(a)
    print(twoSum(a,target))
