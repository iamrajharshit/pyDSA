str1="Hello World"
print(str1)
print(len(str1))

print(str1[1],
      str1[1:4])

#str1[0]="o" #cant be done its immutable

#Concatinate
str2="I am Raj"
strCat=str1+" "+str2
print(strCat)

#print formatting

first="Raj"
last="Harshit"
age="22"

print(f"My name is {first} {last} and my age is {age}")

print("My name is {} {} and my age is {}".format(first,last,age))
