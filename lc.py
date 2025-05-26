class UnionFind:
    def __init__(self, n):
        self.parent = [for i in range(1, n+1)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
            self.parent[x] = self.parent[self.parent[x]]
        
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False
            
        if self.rank[rootX] >= self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
            return True
        
        self.parent[rootX] = rootY
        self.rank[rootY] += self.rank[rootX]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

