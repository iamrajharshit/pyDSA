
# Insertion Sort
# sorted [0] then we compare and swap to the left!

# -Is not the fast sorting algo as it uses nested loops to sort.
# -Only useful for small data sets (no more than 10,000 items)
# -It runs in O(n2)



#CODE
A=[23,45,67,32,1,45,6,2,67,3]

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
    print(A)



# def inser_while(A):
#     for i in range(1,len(A)):
#         j=i-1
#         while A[j]>A[j+1] and j>=0:
#              A[j],A[j+1]=A[j+1],A[j]
#              j-=1

#     return A
x=insertion_sort(A)
