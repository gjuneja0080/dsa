# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)

        dfs(root)
        
        def build_tree(nums):

            if not nums: return None
            
            mid = len(nums) // 2
            
            node = TreeNode(nums[mid])
            
            node.left = build_tree(nums[:mid])
            node.right = build_tree(nums[mid+1:])
            
            return node
        
        res = build_tree(lst)
        
        return res
