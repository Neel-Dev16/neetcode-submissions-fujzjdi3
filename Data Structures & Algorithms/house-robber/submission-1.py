class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def f(x:int)->int:
            if x in memo:
                return memo[x]
            if x<0:
                return 0
            if x==0:
                return nums[0]
            memo[x]=max(f(x-1), nums[x]+ f(x-2))
            return memo[x]
        return f(len(nums)-1)

        