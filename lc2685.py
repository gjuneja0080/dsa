class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            component.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        ans = 0
        visited = set()
        for vertex in range(n):
            if vertex not in visited:
                component = set()
                visited.add(vertex)
                dfs(vertex)

                isComplete = True
                for node in component:
                    if len(component) - 1 != len(graph[node]):
                        isComplete = False
                        break

                if isComplete:
                    ans += 1
        return ans

                     
