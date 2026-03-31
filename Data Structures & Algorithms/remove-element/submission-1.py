class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=[]
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            res.append(nums[i])
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)