class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(crs):
            if crs in visited: return False
            if graph[crs] == []: return True
            
            visited.add(crs)
            for prereq in graph[crs]:
                if not dfs(prereq): return False
            visited.remove(crs)
            graph[crs] = []
            
            return True

        visited = set()
        for i in range(numCourses):
            if not dfs(i): return False
        return True
