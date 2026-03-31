class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        total =0
        def dfs(i,total):
            if i==n:
                return total
            return dfs(i+1,total^nums[i]) + dfs(i+1,total)
        return dfs(0,0)
        