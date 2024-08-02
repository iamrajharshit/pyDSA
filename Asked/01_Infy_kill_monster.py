# def fibo(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibo(n-1)+fibo(n-2)

# print(fibo(4))



# def max_monsters(n, e, monsters):
#     monsters.sort(key=lambda x: x[0])  # Sort by power
#     count = 0

#     for power, bonus in monsters:
#         if e >= power:
#             count += 1
#             e += bonus
#         else:
#             break
    
#     return count

# # Test case
# n = 2
# e = 123
# monsters = [(78, 10), (130, 0)]
# print(max_monsters(n, e, monsters))  # Output: 2





def input_num():
    mons = []
    bonus = []
    num = int(input())
    exp = int(input())

    for _ in range(num):
        mons.append(int(input()))

    for _ in range(num):
        bonus.append(int(input()))

    mons_b_dict= dict(sorted(zip(mons,bonus)))
    print(mons_b_dict)

    

    def kill(exp,mons_b_dict):
        c=0
        
        for key, value in mons_b_dict.items():
            if exp >= key:
                exp +=value
                c=c+1

        return c
    
    ans= kill(exp,mons_b_dict)

    return ans

# Call the function and print the result
result = input_num()
print(result)
