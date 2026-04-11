class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        n=len(nums)
        res=[]
        for j in count:
            if count[j]>n//3:
                res.append(j)
        return res