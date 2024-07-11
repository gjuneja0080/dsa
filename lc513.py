# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leftmost_val = root.val
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if i == 0:
                    leftmost_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftmost_val
#################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level_dict = defaultdict(list)
        def dfs(node, level):
            if not node: return
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
            level_dict[level].append(node.val)
        dfs(root, 1)
        return level_dict[max(level_dict.keys())][0]
            



            
            
