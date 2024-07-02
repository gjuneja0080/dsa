"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        queue = deque([root])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if i != qlen - 1:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root
########################################################################################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def findNext(node):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            return None

        def dfs(node):
            if not node: return
            if not node.left and not node.right: return node
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = findNext(node.next)
            if node.right:
                node.right.next = findNext(node.next)
            dfs(node.right)
            dfs(node.left)
            return node

        return dfs(root)
        
