class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visit, cycle = set(), set()
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)  

        def dfs(course):
            if course in cycle: return False
            if course in visit: return True
            cycle.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        
        return res
