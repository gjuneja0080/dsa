class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        res = [[] for _ in range(n)]
        indegree = {i: 0 for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([v for v in indegree if indegree[v] == 0])
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                res[nei].append(node)
                res[nei] += res[node]
                combined_set = set(res[nei]) | set(res[node])
                res[nei] = list(combined_set)
                res[nei].sort()
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res
