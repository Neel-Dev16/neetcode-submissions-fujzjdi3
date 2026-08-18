class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {(0, 0): 1}

        for i in range(len(nums)):
            nxt = {}
            for (_, total), count in dp.items():
                nxt[(i + 1, total + nums[i])] = nxt.get((i + 1, total + nums[i]), 0) + count
                nxt[(i + 1, total - nums[i])] = nxt.get((i + 1, total - nums[i]), 0) + count
            dp = nxt
        return dp.get((len(nums), target), 0)
