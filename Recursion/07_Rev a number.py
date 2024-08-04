result=0

def re1(n):
    global result
    if n==0:
        return
    rem = n%10
    result =(result*10)+rem
    # print(result)
    re1(n//10)

def main():
    global result
    re1(1234)
    print(result)
    

main()