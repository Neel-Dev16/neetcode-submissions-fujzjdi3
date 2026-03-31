class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1= [0]*26
        for i in range(len(s)):
            s1[ord(s[i])- ord('a')]+=1
            s1[ord(t[i])- ord('a')]-=1
        for val in s1:
            if val !=0:
                return False
        return True
      