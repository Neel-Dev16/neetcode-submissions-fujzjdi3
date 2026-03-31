class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        fresh=0
        time=0
        visit=set()
        q=deque()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        while q and fresh>0:
            time+=1
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    row,col=r+dr,c+dc
                    if (row in range(len(grid)) and col in range(len(grid[0]))and grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1
        return time if fresh==0 else -1
        