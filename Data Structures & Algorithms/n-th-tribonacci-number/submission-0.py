class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def f(k):
            if k in memo:
                return memo[k]
            if k==0:
                return 0
            if k==1 or k==2:
                return 1
            memo[k] = f(k-1) + f(k-2) + f(k-3)
            return memo[k]
        return f(n)
        