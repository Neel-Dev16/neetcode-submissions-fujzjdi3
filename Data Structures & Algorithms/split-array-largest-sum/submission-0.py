class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            limit = (l + r) // 2
            parts = 1
            cur = 0
            for n in nums:
                if cur + n > limit:
                    parts += 1
                    cur = 0
                cur += n

            if parts <= k:
                res = limit
                r = limit - 1
            else:
                l = limit + 1
        return res
