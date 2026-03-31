class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=collections.defaultdict(list)
        res=[]
        for src,des in tickets:
            adj[src].append(des)
        for src in adj:
            adj[src].sort(reverse=True)
        def dfs(airport):
            while adj[airport]:
                next_airport=adj[airport].pop()
                dfs(next_airport)
            res.append(airport)
        dfs("JFK")
        return res[::-1]