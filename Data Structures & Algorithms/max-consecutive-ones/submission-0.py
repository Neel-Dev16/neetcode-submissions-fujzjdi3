class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        track=0
        for i in range(len(nums)):
            if nums[i]==1:
                track+=1
            else:
                res=max(res,track)
                track=0
        return max(res,track)
        