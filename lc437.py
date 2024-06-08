# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        res = 0
        
        def dfs(node, prefix_sum, prefix_dict):
            nonlocal res
            if not node: return 0
            if (prefix_sum - targetSum) in prefix_dict:
                res += prefix_dict[prefix_sum - targetSum]
            
            if prefix_sum in prefix_dict:
                prefix_dict[prefix_sum] += 1
            
            else:
                prefix_dict[prefix_sum] = 1
            
            if node.left:
                dfs(node.left, prefix_sum + node.left.val, prefix_dict)
            
            if node.right:
                dfs(node.right, prefix_sum + node.right.val, prefix_dict)
            
            prefix_dict[prefix_sum] -= 1

        dfs(root, root.val, {0: 1})
        return res
