# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, num):
            nonlocal total
            if not node.left and not node.right:
                total += int(num + str(node.val))
                return 
            if node.left:
                dfs(node.left, num + str(node.val))
            if node.right:
                dfs(node.right, num + str(node.val))
        dfs(root, '')
        return total
