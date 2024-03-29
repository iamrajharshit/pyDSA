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






