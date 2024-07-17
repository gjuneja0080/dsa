# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def dfs(node, previous, direction):
            if not node: return
            if node.left: dfs(node.left, node, 'left')
            if node.right: dfs(node.right, node, 'right')

            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                if direction == 'left':
                    previous.left = None
                elif direction == 'right':
                    previous.right = None

        res = []
        to_delete = set(to_delete)
        dfs(root, None, '')
        if root.val not in to_delete:
            res.append(root)
        return res
