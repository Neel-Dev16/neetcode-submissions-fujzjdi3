import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, price in flights:
            adj[s].append([d, price])

        heap = [[0, src, 0]]
        stops = {}
        while heap:
            cost, node, stop = heapq.heappop(heap)
            if node == dst:
                return cost
            if stop > k or stop > stops.get(node, float('inf')):
                continue
            stops[node] = stop
            for nei, price in adj[node]:
                heapq.heappush(heap, [cost + price, nei, stop + 1])
        return -1
