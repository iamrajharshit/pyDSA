'''Write a py p to find out commmon letters btw two strings'''

def common_letters():
    str1=input("Enter first string: ")
    str2=input("Enter 2nd string: ")

    #to make the string unique
    s1=set(str1)
    s2=set(str2)
    # & is used to get common string 
    com=s1&s2
    print(com)
    # print(s1)
    # print(s2)

common_letters()