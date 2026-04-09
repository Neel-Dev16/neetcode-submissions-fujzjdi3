class Solution:
    def scoreOfString(self, s: str) -> int:
        res=[0]*len(s)
        for i in range(len(s)):
            res[i]=ord(s[i])
        i,j=0,1
        ans=0
        for j in range(1,len(res)):
            ans+=abs(res[j]-res[i])
            i+=1
        return ans

        