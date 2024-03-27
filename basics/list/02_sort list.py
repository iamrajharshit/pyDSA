#without sorted keyword

list1=[32,45,12,54,56,23]

n=len(list1)

for i in range(n):
    for j in range(i+1,n):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]


print(list1)

