class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        rank = [0]*n
        parent=list(range(n))

        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x= parent[x]
            return x
        def union(a,b):
            ra,rb= find(a), find(b)
            if ra==rb:
                return 0
            if rank[ra]<rank[rb]:
                parent[ra]=rb
            elif rank[ra]>rank[rb]:
                parent[rb]=ra
            else:
                parent[rb]=ra
                rank[ra]+=1
            return 1
        for a,b in edges:
            components -=union(a,b)
        return components
        