class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False

        target = sum(nums) // k
        used = [False] * len(nums)
        nums.sort(reverse=True)

        def backtrack(i, cur, groups):
            if groups == k:
                return True
            if cur == target:
                return backtrack(0, 0, groups + 1)

            prev = -1
            for j in range(i, len(nums)):
                if used[j] or cur + nums[j] > target or nums[j] == prev:
                    continue
                used[j] = True
                if backtrack(j + 1, cur + nums[j], groups):
                    return True
                used[j] = False
                prev = nums[j]
                if cur == 0:
                    break
            return False

        return backtrack(0, 0, 0)
