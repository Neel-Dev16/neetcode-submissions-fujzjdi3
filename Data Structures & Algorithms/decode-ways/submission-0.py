class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={}
        def f(x):
            if x in memo:
                return memo[x]
            if x==n:
                return 1
            if s[x]=="0":
                return 0
            ways = f(x+1)
            if x+1<n and 10<=(int(s[x:x+2]))<=26:
                ways+=f(x+2)
            memo[x]=ways
            return ways
        return f(0)
        