class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(current_node, next_node):
            if current_node == next_node:
                return True
            
            visited.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    if dfs(neighbor, next_node):
                        return True
            return False

        graph = defaultdict(list)
        for u, v in edges:
            visited = set()
            if dfs(u, v):
                return [u, v]
            else:
                graph[u].append(v)
                graph[v].append(u)
