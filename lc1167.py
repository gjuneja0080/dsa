class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        total_cost = 0
        count = lensum = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:

            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            combined_cost = stick1 + stick2
            total_cost += combined_cost
            heapq.heappush(sticks, combined_cost)
            
        return total_cost
