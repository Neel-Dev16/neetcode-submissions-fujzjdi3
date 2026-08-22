from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(edges):
            adj = defaultdict(list)
            indeg = [0] * (k + 1)
            for a, b in edges:
                adj[a].append(b)
                indeg[b] += 1

            q = deque([i for i in range(1, k + 1) if indeg[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            return order if len(order) == k else []

        rows = topo(rowConditions)
        cols = topo(colConditions)
        if not rows or not cols:
            return []

        rowPos = {n: i for i, n in enumerate(rows)}
        colPos = {n: i for i, n in enumerate(cols)}
        res = [[0] * k for _ in range(k)]
        for n in range(1, k + 1):
            res[rowPos[n]][colPos[n]] = n
        return res
