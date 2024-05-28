class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if maxCost == 0:
            if s == t: return len(s)
            else: return 1
        
        cost = []
        lp = 0
        total_cost = 0
        elements = 0
        max_elements = 0
        for i in range(len(s)):
            cost.append(abs(ord(s[i]) - ord(t[i])))

        for rp in range(len(cost)):
            total_cost += cost[rp]
            elements += 1
            while total_cost > maxCost:
                total_cost -= cost[lp]
                lp += 1
                elements -= 1
            if max_elements < elements:
                max_elements = elements
        return max_elements
