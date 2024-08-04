def min_moves(N):

    c=0

    while N>1:
        if N%3==0:
            N//=3

        elif N%2==0:
            N//=2

        else:
            N-=1
        c+=1

    return c


print(min_moves(2))