# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def find_two_swapped(res):
            x = y = None
            for i in range(len(res) - 1):
                if res[i + 1] < res[i]:
                    y = res[i + 1]
                    if x is None:
                        x = res[i]
                    else:
                        break
            return x, y
        
        def recover(node, count):
            if node:
                if node.val == x or node.val == y:
                    node.val = y if node.val == x else x
                    count -= 1
                    if count == 0: return
                recover(node.left, count)
                recover(node.right, count)

        res = inorder(root)
        x, y = find_two_swapped(res)
        recover(root, 2)
        

