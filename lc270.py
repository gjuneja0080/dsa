# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        mindiff, minval = float('inf'), 0
        def dfs(node):
            if not node: return
            nonlocal mindiff, minval
            diff = abs(node.val - target)
            if diff < mindiff:
                mindiff = diff
                minval = node.val
            elif diff == mindiff:
                minval = min(node.val, minval)
            if target < node.val: dfs(node.left)
            else: dfs(node.right)

        dfs(root)
        return minval
