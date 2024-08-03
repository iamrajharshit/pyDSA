# height=[2,1,3,4,5,6,7,8]
# p=[0]*len(height) #init p with zeros
# p[0]=height[0]

# for i in range(1,len(height)):
#     p[i]=max(p[i-1],height[i])

# print(p)

# p=[height[0]]
# print(p)
# for i in range(1,len(height)):
#      p.append(max(p[-1], height[i]))
# print(p)    

height = [0,1,0,2,1,0,1,3,2,1,2,1]

def sol1(height):
    prif=[]
    for i in range(0,len(height)):
        prif.append(max(height[0:i+1]))

    print(prif)

    suff=[]
    for i in range(0,len(height)):
        suff.append(max(height[i:len(height)]))

    print(suff)

    total =0

    for i in range(len(height)):
            total+=min(suff[i],prif[i])-height[i]

    return total

#my sol

def trappingWater(self, arr,n):
    
        total=0
        
        suff=[0]*n
        prif=[0]*n
        
        suff[0]=arr[0]
        for i in range(1,n):
            suff[i]=max(suff[i-1],arr[i])
               
        prif[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            prif[i]=max(arr[i],prif[i+1])

        
        for i in range(n):
            total+=min(suff[i],prif[i])-arr[i]
            
        return total





#2 pointer
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        if not arr:
            return 0
            
            
        n = len(arr)
        
        left,right = 0 ,n-1
        left_max,right_max = arr[left],arr[right]
        
        water_trapped = 0
        
        while left < right:
            if arr[left] < arr[right]:
                left += 1
                left_max = max(left_max,arr[left])
                water_trapped += left_max - arr[left]
            
            else:
                right -= 1
                right_max = max(right_max,arr[right])
                water_trapped += right_max - arr[right]
                
        return water_trapped
 




