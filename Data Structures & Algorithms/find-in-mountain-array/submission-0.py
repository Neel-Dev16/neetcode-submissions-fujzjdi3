class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l

        def search(l, r, asc):
            while l <= r:
                m = (l + r) // 2
                val = mountainArr.get(m)
                if val == target:
                    return m
                if asc:
                    if val < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if val < target:
                        r = m - 1
                    else:
                        l = m + 1
            return -1

        left = search(0, peak, True)
        return left if left != -1 else search(peak + 1, n - 1, False)
