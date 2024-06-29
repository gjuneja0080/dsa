class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(node):
            queue = deque([node])
            while queue:
                current_node = queue.popleft()
                for neighbor in range(n):
                    if isConnected[current_node][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        comp_count = 0
        visited = set()
        n = len(isConnected)
        for i in range(n):
            if i not in visited:
                visited.add(i)
                comp_count += 1
                bfs(i)

        return comp_count


################################################################################################

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        comp_count = 0
        visited = set()
        n = len(isConnected)
        for i in range(n):
            if i not in visited:
                visited.add(i)
                comp_count += 1
                dfs(i)

        return comp_count
