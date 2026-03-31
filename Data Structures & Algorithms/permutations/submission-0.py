class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        used=[False]*n
        def dfs(cur):
            if len(cur)==n:
                res.append(cur.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i]=True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                used[i]=False
        dfs([])
        return res
            
        