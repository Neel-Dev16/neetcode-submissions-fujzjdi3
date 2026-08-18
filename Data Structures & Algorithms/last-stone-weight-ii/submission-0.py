class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = set([0])

        for s in stones:
            nxt = set(dp)
            for total in dp:
                if total + s <= target:
                    nxt.add(total + s)
            dp = nxt
        return sum(stones) - 2 * max(dp)
