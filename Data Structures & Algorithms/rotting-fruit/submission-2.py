class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        fresh=0
        time=0
        q=deque()
        directions =[[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        while q and fresh>0:
            time+=1
            for i in range(len(q)):
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (0<=r<rows and 0<=c<cols and grid[r][c]==1):
                        grid[r][c]=2
                        fresh-=1
                        q.append((r,c))
        return time if fresh==0 else -1
