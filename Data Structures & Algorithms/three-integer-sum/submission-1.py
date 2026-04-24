class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        threeSum=0
        nums.sort()
        for i,v in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if v>0:
                break
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum= v + nums[l] + nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append((v,nums[l],nums[r]))
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res
            
        