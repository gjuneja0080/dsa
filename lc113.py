# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, total, path):
            if not node: return
            path.append(node.val)
            if not node.left and not node.right:
                if total + node.val == targetSum:
                    res.append(path.copy())
            dfs(node.left, total + node.val, path)
            dfs(node.right, total + node.val, path)
            path.pop()

        res = []
        dfs(root, 0, [])
        return res
        
