"""
Three Sum Problem:
Obj: A+B+C+=0
Find all unique triplets 
"""
arr=[3,5,23,5,-8,-3,-2,-2,-4,-6]

def threesum(arr):
    res=[]
    arr.sort()

    for i in range(len(arr)-2):
        l=i+1
        r=len(arr)-1
        if i>0 and arr[i]==arr[i-1]:
            #i=i+1
            continue
        
        while(l<r):
            total=arr[i]+arr[l]+arr[r]
            if total <0:
                l=l+1
            elif total>0:
                r=r-1
            else:
                res.append([arr[i],arr[l],arr[r]])

                while l<r and arr[l]== arr[l+1]:
                    l=l+1
                while l<r and arr[r]== arr[r-1]:
                    r=r-1

                l=l-1
                r-=1
    return res

print(threesum(arr))

#[[-8, 3, 5], [-3, -2, 5]]