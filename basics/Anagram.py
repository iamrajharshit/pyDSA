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




         