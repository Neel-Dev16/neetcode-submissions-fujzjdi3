class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        left,right=0,(rows*cols)-1
        while left<=right:
            mid = left + (right-left)//2
            r= mid//cols
            c= mid%cols
            val=matrix[r][c]
            if val == target:
                return True
            elif val > target:
                right = mid-1
            else:
                left = mid + 1
        return False        