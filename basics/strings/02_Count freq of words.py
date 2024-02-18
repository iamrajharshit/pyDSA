'''Write a py p to Count the freq of words appearing in a string'''

eg="Sheela loves eating apple and mango. Her sister also loves eating apple and mango"
def freq(str):
    #str=input("Enter a string")

    li=str.split() #split into words and return in form of list 
    d={}

    for i in li:
        if i not in d.keys():
            #key=value is used
            d[i]=0
        d[i]=d[i]+1

    print(d)

freq(eg)