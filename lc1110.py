# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, previous, direction):
            if not node: return None
            if node.left: dfs(node.left, node, 'left')
            if node.right: dfs(node.right, node, 'right')
            
            if (node.val in to_delete) and (node.val not in visited):
                visited.add(node.val)
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                if direction == 'left':
                    previous.left = None
                elif direction == 'right':
                    previous.right = None 
        res = []
        visited = set()
        dfs(root, None, '')
        if root.val not in to_delete:
            res.append(root)
        return res
