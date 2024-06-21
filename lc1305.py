# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(node, lst):
            if not node: return
            dfs(node.left, lst)
            lst.append(node.val)
            dfs(node.right, lst)
            return lst
        if not root1 and not root2:
            return []
        else:
            res = []
            i, j, res_p = 0, 0, 0
            lst1 = dfs(root1, [])
            lst2 = dfs(root2, [])
            if not lst1 and lst2:
                lst2.sort()
                return lst2
            elif lst1 and not lst2:
                lst1.sort()
                return lst1
            while i < len(lst1) and j < len(lst2):
                if lst1[i] <= lst2[j]:
                    res.append(lst1[i])
                    i += 1
                else:
                    res.append(lst2[j])
                    j += 1

            while i < len(lst1):
                res.append(lst1[i])
                i += 1
            while j < len(lst2):
                res.append(lst2[j])
                j += 1
            
            return res
