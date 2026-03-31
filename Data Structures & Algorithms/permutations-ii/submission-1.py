class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        used=[False]*n
        def dfs(cur):
            if len(cur)==n:
                res.append(cur.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                used[i]=False
        dfs([])
        return res
        