class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()[::-1]
        cnt=0
        for i in s:
            if i.isalnum():
                cnt+=1
            else:
                return cnt
        return cnt
        