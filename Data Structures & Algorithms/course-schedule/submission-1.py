class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finished=0
        while q:
            node=q.popleft()
            finished+=1
            for nei in preMap[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return finished==numCourses