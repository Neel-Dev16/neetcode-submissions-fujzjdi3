class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def f(k):
            if k in memo:
                return memo[k]
            if k==1 or k==0:
                return cost[k]
            memo[k]= cost[k] + min(f(k-1),f(k-2))
            return memo[k]
        n=len(cost)
        return min(f(n-1),f(n-2))
        