arr=[1,2,3,4,5]

temp=arr[0]

print(arr)
for i in range(1,len(arr)):
    arr[i-1]=arr[i]

arr[len(arr)-1]=temp

print(arr)

# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 1]