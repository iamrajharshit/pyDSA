'''Givrn array, find the next greater element G[i] for every element A[i]
in array. The Next greater Element for an element A[i] is the greater element on 
the right side of A[i] in array.

Input: [4,5,2,10]
Output:[5,10,10,-1]

Input:[3,2,1]
Output:[-1,-1,-1]
'''
def nextGen(A):
    n = len(A)  # Length of the input array
    stack = []  # Initialize an empty stack to hold elements and their indices
    nge = [-1] * len(A)  # Initialize an array to store the next greater elements, initialized with -1

    # Iterate over the elements of the input array along with their indices
    for i, A in enumerate(A):
        # While the stack is not empty and the top element of the stack is less than the current element
        while stack and stack[-1][0] < A:
            # Pop the top element from the stack and update its next greater element to the current element
            nge[stack.pop()[1]] = A

        # Push the current element and its index onto the stack
        stack.append((A, i))

    # Return the array containing the next greater elements
    return nge



A=[4,5,2,10]    
x=nextGen(A)
print(x)
