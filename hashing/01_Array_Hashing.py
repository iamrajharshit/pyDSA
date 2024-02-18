#find the freq using hash map and where k is most freq elements is returned
# O(n) for hashmap
# time comp O(n+n) which is O(n)

class sol(object):

    def topKfrq(self, nums, k):
        hmap={}
        # creating an empty list 
        count_lst=[[] for i in range(len(nums) + 1)]
        
        ret_lst = []

        for n in nums:
            hmap[n]= hmap.get(n,0) + 1

        for key, val in hmap.items():
            count_lst[val].append(key)

        for i in range(len(count_lst) -1, 0,-1):
            for j in count_lst[i]:
                ret_lst.append(j)

                if k == len(ret_lst):
                    return ret_lst
        return []        

nums=[1,1,1,2,2,3,3,3,3,3,3,3]
k=2

b=sol()
print(b.topKfrq(nums,k))