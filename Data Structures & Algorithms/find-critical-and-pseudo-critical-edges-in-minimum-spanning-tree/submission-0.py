class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda x: x[2])

        def mst(skip=-1, include=-1):
            parent = [i for i in range(n)]
            rank = [1] * n

            def find(x):
                while x != parent[x]:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                pa, pb = find(a), find(b)
                if pa == pb:
                    return False
                if rank[pa] < rank[pb]:
                    pa, pb = pb, pa
                parent[pb] = pa
                rank[pa] += rank[pb]
                return True

            weight = 0
            count = 0
            if include != -1:
                a, b, w, _ = edges[include]
                union(a, b)
                weight += w
                count += 1

            for i, (a, b, w, _) in enumerate(edges):
                if i == skip:
                    continue
                if union(a, b):
                    weight += w
                    count += 1
            return weight if count == n - 1 else float('inf')

        best = mst()
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            if mst(skip=i) > best:
                critical.append(e[3])
            elif mst(include=i) == best:
                pseudo.append(e[3])
        return [critical, pseudo]
