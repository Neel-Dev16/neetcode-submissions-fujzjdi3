class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap=[]
        minHeap=[[c,p] for c,p in zip(capital,profits)]
        heapq.heapify(minHeap)
        for _ in range(k):
            while minHeap and minHeap[0][0]<=w:
                cost,profit=heapq.heappop(minHeap)
                heapq.heappush(maxHeap,-profit)
            if not maxHeap:
                break
            w+=-heapq.heappop(maxHeap)
        return w

        