class Solution:
    def numSquares(self, n: int) -> int:
        memo={}
        def f(x:int)->int:
            if x in memo:
                return memo[x]
            if x==0:
                return 0
            best = float('inf')
            j=1
            while j*j <= x:
                sq=j*j
                best =min(best,1 + f(x-sq))
                j+=1
            memo[x]=best
            return best
        return f(n)
