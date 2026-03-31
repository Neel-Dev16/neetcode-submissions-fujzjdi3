class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        perimeter=0
        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            perimeter=dfs(r+1,c)
            perimeter+=dfs(r-1,c)
            perimeter+=dfs(r,c+1)
            perimeter+=dfs(r,c-1)
            return perimeter


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    return dfs(r,c)

        