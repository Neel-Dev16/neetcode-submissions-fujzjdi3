class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]

            total = 0
            dp[i] = float('-inf')
            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j]
                dp[i] = max(dp[i], total - dfs(j + 1))
            return dp[i]

        score = dfs(0)
        if score > 0:
            return 'Alice'
        if score < 0:
            return 'Bob'
        return 'Tie'
