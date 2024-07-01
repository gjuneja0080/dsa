"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return 
        clone_dict = {}
        def clone(node):
            if node in clone_dict: return clone_dict[node]
            clone_node = Node(node.val)
            clone_dict[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            return clone_node
        
        return clone(node)
