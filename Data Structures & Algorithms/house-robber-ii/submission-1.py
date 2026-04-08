class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        money1=self.rob_linear(nums[:-1])
        money2=self.rob_linear(nums[1:])
        return max(money1,money2)
        
        
        
        
        
    def rob_linear(self,nums):
        memo={}
        n=len(nums)
        def f(i):
            if i in memo:
                return memo[i]
            if i>=n:
                return 0
            skip = f(i+1)
            take = nums[i] + f(i+2)
            memo[i]=max(skip,take)
            return memo[i]
        return f(0)
        