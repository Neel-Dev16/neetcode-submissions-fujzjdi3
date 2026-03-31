class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial = image[sr][sc]
        rows,cols = len(image), len(image[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        if initial == color:
            return image
        q=deque([(sr,sc)])
        image[sr][sc]=color
        while q:
            r,c= q.popleft()
            for dr,dc in directions:
                row,col= r+dr,c+dc
                if (row in range(rows) and col in range(cols) and image[row][col]==initial):
                    image[row][col]=color
                    q.append((row,col))
        return image
        