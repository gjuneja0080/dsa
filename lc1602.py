# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque([root])
        rightmost = None
        while q:
            qlen = len(q)
            prev = None
            for i in range(len(q)):
                node = q.popleft()
                if prev != None:
                    rightmost = node
                    break
                if node == u:
                    prev = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if rightmost: break
        return rightmost
