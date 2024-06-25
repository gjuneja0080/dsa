# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def dfs(node):
            if not node: return 0

            len_left = dfs(node.left)
            len_right = dfs(node.right)
            
            left_path, right_path = 0, 0

            if node.left and node.left.val == node.val:
                left_path = len_left + 1
            if node.right and node.right.val == node.val:
                right_path = len_right + 1

            self.longest_path = max(self.longest_path, left_path + right_path)

            return max(left_path, right_path)
        dfs(root)
        return self.longest_path
