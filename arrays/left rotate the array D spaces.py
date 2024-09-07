arr=[1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7]
print(arr)
d=9
d=d % len(arr)

new=arr[0:d]

arr[0:d]=[]

arr.extend(new)

print(arr)