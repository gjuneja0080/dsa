# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def find_maxind(lst):
            maxind = 0
            for i in range(1, len(lst)):
                if lst[i] > lst[maxind]:
                    maxind = i
            
            return maxind

        def build_tree(lst):
            if not lst: return None
            maxind = find_maxind(lst)

            root = TreeNode(lst[maxind])
            root.left = build_tree(lst[:maxind])
            root.right = build_tree(lst[maxind+1:])
            return root

        res = build_tree(nums)
        return res
