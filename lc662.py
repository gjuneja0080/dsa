# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([[root, 0, 0]])           # deque([[root, num, level]])
        prevlevel, prevnum = 0, 0
        while q:
            node, num, level = q.popleft()

            if level > prevlevel:
                prevnum = num
                prevlevel = level

            res = max(res, num - prevnum + 1)
            
            if node.left: q.append([node.left, num * 2, level + 1])
            if node.right: q.append([node.right, num * 2 + 1, level + 1])
 
        return res