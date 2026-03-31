class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        if "0000" in dead:
            return -1
        if "0000" == target:
            return 0
        q=deque(["0000"])
        steps=0
        visit=set(["0000"])

        while q:
            steps+=1
            for _ in range(len(q)):
                lock=q.popleft()

                for i in range(4):
                    d=int(lock[i])
                    for move in (-1,1):
                        nd=(d+move)%10
                        nxt=lock[:i]+str(nd)+lock[i+1:]

                        if nxt in dead or nxt in visit:
                            continue
                        if nxt==target:
                            return steps
                        visit.add(nxt)
                        q.append(nxt)
        return -1



        