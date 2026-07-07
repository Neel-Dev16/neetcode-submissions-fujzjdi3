class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        cur = 0
        res = 0

        for n in nums:
            cur += n
            res += count.get(cur - k, 0)
            count[cur] = 1 + count.get(cur, 0)
        return res
