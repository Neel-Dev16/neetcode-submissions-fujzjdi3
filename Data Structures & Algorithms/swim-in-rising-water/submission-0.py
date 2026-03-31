class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            time,r,c= heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if r==n-1 and c==n-1:
                return time
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0 <= nc < n and (nr, nc) not in visit:
                    newTime = max(time, grid[nr][nc])
                    heapq.heappush(minHeap, (newTime, nr, nc))
        
        