class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        prod=1
        for num in nums:
            if num==0:
                zeros+=1
                if zeros>1:
                    return [0]*len(nums)
            else:
                prod=prod*num
        res=[0]*len(nums)
        for i in range(len(nums)):
            if zeros==1:
                if nums[i]==0:
                    res[i]=prod
            else:
                res[i]=prod//nums[i]
        return res
