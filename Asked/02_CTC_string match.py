'''Given string wiith white space in between,
0th index gives length of the string
1st index part 1 of the string1 
then string2 follows


match string1 with string2 
if element matches pop that element from both the string
else rotate string1 push that unmatched element at the last index
count the number of operations.
 '''

s='5 6 4 1 2 3 6 3 1 2 4'
swith="".join(s.split())
#print(swith)
n=int(swith[0])

st1=[]
st2=[]
c=0
for i in range(1,n+1):
    st1.append(swith[i])

for j in range(n+1,len(swith)):
    st2.append(swith[j])

while st1 and st2:
    if st1[0]==st2[0]:
        st1.pop(0)
        st2.pop(0)
        c=c+1

    else:
        x=st1.pop(0)
        st1.append(x)
        c=c+1

print(c)