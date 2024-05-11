# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return 
        res = []
        level = 0
        q = deque([[root, 0]])
        level_dict = defaultdict(list)

        while q:
            qlen = len(q)
            for i in range(qlen):
                node, level = q.popleft()
                level_dict[level].append(node.val)
                if node.left: q.append([node.left, level + 1])
                if node.right: q.append([node.right, level + 1])
        
        for i in range(level, -1, -1):
            res.append(level_dict[i])
        return res