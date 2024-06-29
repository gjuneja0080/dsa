class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(current_node):
            visited[current_node] = True
            for next_node in graph[current_node]:
                if not visited[next_node]:
                    dfs(next_node)

        comp_count = 0
        visited = [False] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                comp_count += 1
        return comp_count


##############################################################################
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp_count = 0
        visited = [False] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(current_node):
            nonlocal comp_count
            queue = deque([current_node])
            visited[current_node] = True
            while queue:
                current_node = queue.popleft()
                for next_node in graph[current_node]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        queue.append(next_node)

        for i in range(n):
            if not visited[i]:
                comp_count += 1
                bfs(i)

        return comp_count
