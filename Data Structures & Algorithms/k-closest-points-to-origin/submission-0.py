class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for x,y in points:
            add=(x**2) + (y**2)
            res.append([add,x,y])
        heapq.heapify(res)
        ans=[]
        while k>0:
            dist,x,y=heapq.heappop(res)
            ans.append([x,y])
            k-=1
        return ans
        