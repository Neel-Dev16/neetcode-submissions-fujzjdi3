import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        heap = [[0, 0, 0]]
        visit = set()

        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    heapq.heappush(heap, [max(effort, diff), nr, nc])
