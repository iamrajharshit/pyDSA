#Concatenate
l1=[1,2,3,4,5]
l2=[4,6,7,5,7]

lcat=l1+l2
print(lcat)

#Repetition
ll1=["Hello"]
print(ll1*5)

#Membership
ll2=["Amit","Raj","Rohan"]
print("Amit" in ll2)
print("Nitin" in ll2)

#Slicing
ll3=["Amit","Raj","Rohan","Sharma","Harsh","Saachi"]
print(ll3[2:4])
print("Rev",ll3[::-1])
print("first two, rev",ll3[1::-1])
print(ll3[:-3:-1],ll3[:-3:])
