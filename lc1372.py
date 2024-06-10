class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, path, direction):
            if not node:
                return
            nonlocal maxpath
            maxpath = max(path, maxpath)
            
            if direction == 'left' or direction == '':
                dfs(node.left, 1, 'left')
                dfs(node.right, path + 1, 'right')
            elif direction == 'right' or direction == '':
                dfs(node.right, 1, 'right')
                dfs(node.left, path + 1, 'left')

        maxpath = 0
        dfs(root, 0, '')
        return maxpath
