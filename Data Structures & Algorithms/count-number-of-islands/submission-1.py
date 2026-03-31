class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        rows,cols = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        seen=set()
        q=collections.deque()

        if not grid:
            return 0
        def bfs(r,c):
            seen.add((r,c))
            q.append((r,c))
            while q:
                row,col= q.pop()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and
                       c in range(cols) and
                       grid[r][c]=='1' and
                       (r,c) not in seen):
                       q.append((r,c))
                       seen.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =='1' and (r,c) not in seen:
                    bfs(r,c)
                    islands+=1
        return islands