class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False

        parent = {}

        def find(x):
            parent.setdefault(x, x)
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        for n in nums:
            x = n
            p = 2
            while p * p <= x:
                if x % p == 0:
                    union(n, p)
                    while x % p == 0:
                        x //= p
                p += 1
            if x > 1:
                union(n, x)

        root = find(nums[0])
        return all(find(n) == root for n in nums)
