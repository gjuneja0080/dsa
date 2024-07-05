class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            nonlocal res
            passengers = 0
            for child in graph[node]:
                if child != parent:     # just to check if the neighbor being visited isn't the one it came from; so we're not going in cycle
                    p = dfs(child, node) # takes current node and previous node (parent) as argument to avoid revisiting the parent node and creating a cycle
                    passengers += p     # Accumulate passengers from the child subtree
                    res += int(ceil(p / seats)) # Calculate and accumulate trips needed to get to capital for these passengers
            return passengers + 1       # return passengers for the current node's subtree plus itself (also base case as each node (representing a city or town contributes one passenger(itself))

        res = 0
        dfs(0, -1)
        return res

# when a leaf node is reached, the dfs returns 1(itself as passenger), which is effectively the base case
# for non-leaf nodes, it traverses through all child nodes(except the parent to avoid cycling back).
#then accumulates passengers returned from these child nodes and calculates trips required to transport them to the current node
