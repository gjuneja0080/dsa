class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([0])
        visited = [False] * len(rooms)
        visited[0] = True
        
        while queue:
            current_room = queue.popleft()
            for next_room in rooms[current_room]:
                if not visited[next_room]:
                    visited[next_room] = True
                    queue.append(next_room)

        return False if False in visited else True
