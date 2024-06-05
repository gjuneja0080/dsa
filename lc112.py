# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return 0
        add = list()
        add_i = 0
        self.helper(root, add, add_i)
        if targetSum in add:
            return True
        else:
            return False
        
    def helper(self, root, add, add_i):
        
        if root is None:
            return
        add_i += root.val
        if(root.left == None and root.right == None):
            add.append(add_i)
            add_i = 0
        self.helper(root.left, add, add_i)
        self.helper(root.right, add, add_i)
        
        return add
        
        
