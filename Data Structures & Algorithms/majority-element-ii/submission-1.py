class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        cand1, cand2 = None, None

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        for c in (cand1, cand2):
            if c is not None and nums.count(c) > len(nums) // 3 and c not in res:
                res.append(c)
        return res
