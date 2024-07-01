class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:

        graph = defaultdict(list)
        for city_a, city_b, cost in roads:
            a, b = city_a - 1, city_b - 1
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        
        def shortest_path(start_city, graph):
            travel_costs = [float("inf") for _ in range(n)]
            travel_costs[start_city] = 0
            heap = [(0, start_city)]
            min_cost = float("inf")
            while heap:
                travel_cost, current_city = heapq.heappop(heap)
                min_cost = min(min_cost, appleCost[current_city] + (k + 1) * travel_cost)
                
                for neighbor, distance in graph[current_city]:
                    next_cost = travel_cost + distance
                    if next_cost < travel_costs[neighbor]:
                        travel_costs[neighbor] = next_cost
                        heapq.heappush(heap, (next_cost, neighbor))
            return min_cost
        res = []
        for start_city in range(n):
            res.append(shortest_path(start_city, graph))
        return res
