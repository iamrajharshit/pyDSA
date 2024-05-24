'''
Longest Substring Without Repeating Characters
Hint
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

s="abcabcbb"

class  Sliding_Window_Solution:
    def lengthOfLongestSubstring(self,s):
        L= _max=0
        _set= set() #st() will include only unique value

        for r in range(len(s)): #itration
            while s[r] in _set: #till r indexed value is in set perform
                _set.remove(s[L]) #we pass str values perform removal of values 
                L+=1 # left pointer we inc on our string
            _set.add(s[r])
            _max=max(_max,r-L+1)

        return _max
        
ans= Sliding_Window_Solution()
answer=ans.lengthOfLongestSubstring(s)
print(answer)
