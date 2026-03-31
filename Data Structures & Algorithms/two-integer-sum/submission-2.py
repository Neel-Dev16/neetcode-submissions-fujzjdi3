class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={}
        for i,v in enumerate(nums):
            diff=target-v
            if diff in preMap:
                return [preMap[diff],i]
            preMap[v]=i