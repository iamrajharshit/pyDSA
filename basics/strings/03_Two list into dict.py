'''Write a py p to convert two list into a dict'''

l1=['Naina','Kimi','Sheena'] #keys
l2=[852345,76567,691276] #values

def list_to_dict(l1,l2):
    #to map will use zip
    res=dict(zip(l1,l2))
    print(res)
    return res
    
d=list_to_dict(l1,l2)


#to convert to tuple
def dict_to_tup(d):
    for i in d.items():
        print(i)

dict_to_tup(d)        