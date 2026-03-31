class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n=numCourses
        next_courses = [[] for _ in range(n)]   # pre -> courses unlocked
        indegree = [0] * n                      # how many prereqs each course has
        prereqs_of = [set() for _ in range(n)]  # prereqs_of[v] = all prereqs of v

        # Build graph: pre -> course
        for pre, course in prerequisites:
            next_courses[pre].append(course)
            indegree[course] += 1

        # Start with courses that have no prerequisites
        q = deque([c for c in range(n) if indegree[c] == 0])

        while q:
            pre = q.popleft()

            for course in next_courses[pre]:
                # pre is a prerequisite of course
                prereqs_of[course].add(pre)

                # everything needed before pre is also needed before course
                prereqs_of[course] |= prereqs_of[pre]

                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return [u in prereqs_of[v] for u, v in queries]
        