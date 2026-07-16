class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            cap = (l + r) // 2
            need = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    need += 1
                    cur = 0
                cur += w

            if need <= days:
                res = cap
                r = cap - 1
            else:
                l = cap + 1
        return res
