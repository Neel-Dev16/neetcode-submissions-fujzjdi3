from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])

        def dfs(src, dst, seen):
            if src not in graph:
                return -1.0
            if src == dst:
                return 1.0
            seen.add(src)
            for nei, weight in graph[src]:
                if nei in seen:
                    continue
                res = dfs(nei, dst, seen)
                if res != -1.0:
                    return weight * res
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]
