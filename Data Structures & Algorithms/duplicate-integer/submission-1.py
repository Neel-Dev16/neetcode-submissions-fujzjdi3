class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in nums:
            if i in result:
                return True
            result.add(i)
        return False
        