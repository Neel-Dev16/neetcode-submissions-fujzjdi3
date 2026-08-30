class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set([0])
        for n in nums:
            nxt = set(dp)
            for t in dp:
                nxt.add(t + n)
            dp = nxt
        return target in dp
