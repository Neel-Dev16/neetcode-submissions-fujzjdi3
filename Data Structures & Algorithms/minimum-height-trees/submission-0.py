from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = deque([i for i in range(n) if len(adj[i]) == 1])
        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                nei = adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei]) == 1:
                    leaves.append(nei)
        return list(leaves)
