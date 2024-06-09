# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        index_to_alphabet = {i: chr(ord('a') + i) for i in range(26)}
        smallest_phrase = None
        
        def dfs(node, path):
            nonlocal smallest_phrase
            if not node:
                return

            path = index_to_alphabet[node.val] + path

            if not node.left and not node.right:
                if smallest_phrase is None or path < smallest_phrase:
                    smallest_phrase = path

            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
                
        dfs(root, "")
        
        return smallest_phrase
