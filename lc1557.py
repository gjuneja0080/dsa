class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for source, dest in edges:
            indegree[dest] += 1
            outdegree[source] += 1
        for i in range(n):
            if indegree[i] == 0 and outdegree[i] > 0:
                ans.append(i)
        return ans


## OR

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        indegree = defaultdict(int)
        for source, dest in edges:
            indegree[dest] += 1
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        return ans
