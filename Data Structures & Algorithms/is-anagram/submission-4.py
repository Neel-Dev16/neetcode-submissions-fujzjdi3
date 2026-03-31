class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr1=[0]*26
        for i in range(len(s)):
            arr1[ord(s[i])-ord('a')]+=1
            arr1[ord(t[i])-ord('a')]-=1
        for val in arr1:
            if val!=0:
                return False
        return True