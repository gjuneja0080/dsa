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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        queue = deque([root])
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if i != qlen - 1:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
        return root

######################################################################

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if not node: return
            if not node.left and not node.right: return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
