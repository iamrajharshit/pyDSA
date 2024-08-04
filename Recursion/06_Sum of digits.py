'''First Cry!'''
# def dumD(n):
#     total=0
#     if n==0:
#         return total
#     if n==1:
#         return total+1
#     while n>1:
#         total+=n%10
#         dumD(n/10)

#     return total
# print(dumD(1342))

#sum
def SumD(n):
    if n==0:
        return 0
    return (n%10)+SumD(n//10)

print(SumD(55))


#produt
def proD(n):
    if (n%10==n):
        return n
    return (n%10)*proD(n//10)

print(proD(55))