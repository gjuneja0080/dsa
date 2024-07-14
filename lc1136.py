class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        numsem = 0
        visited = set()
        graph = defaultdict(list)
        indegree = {i: 0 for i in range(1, n+1)}
        
        for prevc, nextc in relations:
            graph[prevc].append(nextc)
            indegree[nextc] += 1
        
        queue = deque([v for v in indegree if indegree[v] == 0])
        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                node = queue.popleft()
                n -= 1
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            numsem += 1
            
        return numsem if n == 0 else -1

