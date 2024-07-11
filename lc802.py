class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node):
            if node in safe: return safe[node]
            safe[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor): return safe[node]
            safe[node] = True
            return safe[node]
            
        res = []
        safe = dict()
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
