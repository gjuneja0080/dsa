class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        def dfs(node, previous):
            if node in cycle: return False
            if node in visited: return True
            cycle.add(node)
            for neighbor in graph[node]:
                if neighbor != previous:
                    if not dfs(neighbor, node): return False
            cycle.remove(node)
            visited.add(node)
            return True

        cycle, visited = set(), set()
        noCycle = dfs(0, None)

        if noCycle == False or len(visited) != n:
            return False

        return True
