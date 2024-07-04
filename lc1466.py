class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for a, b in connections:
            graph[a].append(b)
            reverse_graph[b].append(a)

        def dfs(node):
            nonlocal count
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += 1
                    visited.add(neighbor)
                    dfs(neighbor)
            for neighbor in reverse_graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        count = 0
        visited = set()
        visited.add(0)
        dfs(0)
        return count
