def print_n(n):
    if n==1:
        print(1)
        return
    print(n) #5 to 1
    print_n(n-1)
    print(n)  # for 1 to 5

print_n(5)
print("------------------")
print(print_n(5))
