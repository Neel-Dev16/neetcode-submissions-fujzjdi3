class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap=[]
        res=""
        for count,char in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if count!=0:
                heapq.heappush(maxHeap,[count,char])
        while maxHeap:
            count1,char1=heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==char1:
                if not maxHeap:
                    break
                count2,char2=heapq.heappop(maxHeap)
                res+=char2
                count2+=1
                if count2:
                    heapq.heappush(maxHeap,[count2,char2])
                heapq.heappush(maxHeap,[count1,char1])
            else:
                res+=char1
                count1+=1
                if count1:
                    heapq.heappush(maxHeap,[count1,char1])
        return res

        