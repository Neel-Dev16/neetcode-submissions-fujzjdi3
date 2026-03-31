class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def f(k):
            if k in memo:
                return memo[k]

            if k == 0 or k == 1:
                return 1

            memo[k] = f(k - 1) + f(k - 2)
            return memo[k]

        return f(n)
