"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node, depth):
            nonlocal max_depth
            if not node: return 
            max_depth = max(max_depth, depth)
            for child in node.children:
                dfs(child, depth + 1)

        max_depth = 0
        dfs(root, 1)
        return max_depth
