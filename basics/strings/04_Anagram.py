'''Anagram
What is an Anagrams?
-Both strings should be of equal length.
-Both strings should have same chars in same order or diff order.

ex: ABC BAC both are anagram! as length are same and have same set of chars.


'''
#####################################################
#Simple code
# str1=input("Enter string 1")
# str2=input("Enter string 2")

# if len(str1)!=len(str2):
#     print("not")

# else:
#     if sorted(str1) == sorted(str2):
#         print("s")
#     else:
#         print("not")





#list
####################################################
from collections import defaultdict

class Solutions:
    def grAnagram(self,strs: list[str]):
        anagram_map=defaultdict(list)
        result=[]

        for s in strs:
            sorted_s=tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)  
        return result      


strs=['ert','tre','fgh','ggf','yui','iuy']          
s=Solutions()
#print(s.grAnagram(strs))




         