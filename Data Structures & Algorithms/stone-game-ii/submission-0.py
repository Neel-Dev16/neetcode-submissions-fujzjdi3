class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(i, m):
            if i == len(piles):
                return 0
            if 2 * m >= len(piles) - i:
                return sum(piles[i:])
            if (i, m) in dp:
                return dp[(i, m)]

            total = 0
            res = 0
            for x in range(1, 2 * m + 1):
                total += piles[i + x - 1]
                res = max(res, total - dfs(i + x, max(m, x)))
            dp[(i, m)] = res
            return res

        return (sum(piles) + dfs(0, 1)) // 2
