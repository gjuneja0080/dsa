class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for node1, node2, weight in edges:
            self.graph[node1].append((node2, weight))

    def addEdge(self, edge: List[int]) -> None:
        node1, node2, weight = edge
        self.graph[node1].append((node2, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.graph)
        min_heap = [(0, node1)]
        weights_list = [float('inf')] * n
        weights_list[node1] = 0

        while min_heap:
            current_weight, current_node = heapq.heappop(min_heap)
            if current_weight > weights_list[current_node]: continue
            if current_node == node2: return current_weight
            for neighbor, nweight in self.graph[current_node]:
                next_weight = current_weight + nweight
                if next_weight < weights_list[neighbor]:
                    weights_list[neighbor] = next_weight
                    heapq.heappush(min_heap, (next_weight, neighbor))
        return -1
                
    
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
