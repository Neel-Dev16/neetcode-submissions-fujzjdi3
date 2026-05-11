class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=[]
        for i,j in zip(position,speed):
            res.append((i,j))
        res.sort(reverse=True)
        stack=[]
        for p,s in res:
            time=(target-p)/s
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)