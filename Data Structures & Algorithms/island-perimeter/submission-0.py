class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        rows,cols = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>= rows or j<0 or j>=cols or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            per = dfs(i+1,j)
            per +=dfs(i-1,j)
            per +=dfs(i,j+1)
            per +=dfs(i,j-1)
            return per
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return dfs(i,j)
        