'''
input: 4 45 6 43 56
where 0th index is the length (n=4) of the cost, of cutting the rod
will consider index from 1 to n
1: 45
2: 6 
3: 43
4: 56
(index sum = n always) 
(find max element sum as cost)
find max cost
example:
1,1,1,1 : 45+45+45+45 = 180
2,2 : 6+6 = 12
3,1 : 43+45 = 88
4 : 56
answer is 180
'''

#imporve the code
#n=input()
n = '4 45 6 43 56'
n_wos = n.split(" ")
length = len(n_wos)

#containing the cost values in integer data type
cost = []
#loop 1 to length to remove the 1st value as it denotes the length
for g in range(1, length):
    x = int(n_wos[g])
    cost.append(x)

num = len(cost)

def find_max(cost, num):
    if num == 0:
        return 0
    
    max_cost = 0
    for i in range(num):
        max_cost = max(max_cost, cost[i] + find_max(cost, num - i - 1))

    return max_cost

print(find_max(cost, num))
