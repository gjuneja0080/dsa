class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        midres = []
        sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        for i in range(n):
            total_cost += sorted_costs[i][0]
        for j in range(n, 2*n):
            total_cost += sorted_costs[j][1]
        return total_cost
