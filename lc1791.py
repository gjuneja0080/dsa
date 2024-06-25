class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_dict = defaultdict(int)
        for e in edges:
            edge_dict[e[0]] += 1
            edge_dict[e[1]] += 1
        
        for k, v in edge_dict.items():
            if v > 1:
                return k
