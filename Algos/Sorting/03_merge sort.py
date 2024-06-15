'''
intput: A1[]={2,1,2,5,7,1,9,3,6,8,8}
A2[]={2,1,8,3}
Output: A1[]={2,2,1,1,8,8,3,5,6,7,9}

'''
def insertion_sort(A):
    #outer loop to cover 2nd item at indx[1] to very last items in the list
    for i in range(1,len(A)):
        #inner loop that covers from i-1 loop through all the items to i (left) to indx[0] 
        #with a step of -1, we want to move left through the list
        for j in range(i-1,0,-1):
            #comparision item at the right is less then item at left, if true swap
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
            else:
                break #break out of the inner loop
    return A

a1=[2,1,2,5,7,1,9,3,6,8,8]
a2=[2,1,8,3]
def merge_sort(a1,a2):
    a3=[]
    for i in range(len(a1)):
        if a1[i] in a2:
            a3.append(a1[i])
    # for 

print(merge_sort(a1,a2))
