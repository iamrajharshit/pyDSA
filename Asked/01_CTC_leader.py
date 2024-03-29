'''
Given a list
return leader if the number is greater than all of its right side numbers its a leader
last element of the list is always a leader

example: [8,1,2,3,4,7,2]
here: 8,7,2 are leader
'''
n=[11,10,2,9,2,7,3]
max=n[-1]
leader_list=[]
leader_list.append(max)
for i in reversed(range(0,len(n))):
    #print(n[i])
    if n[i]>max:
        max=n[i]
        leader_list.append(max)
leader_list=leader_list[::-1]

print(leader_list)






