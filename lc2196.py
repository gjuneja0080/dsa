# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # treedict = defaultdict(list)
        distnodes = set()
        for parent, child, direction in descriptions:
            if parent not in distnodes:
                distnodes.add(parent)
            if child not in distnodes:
                distnodes.add(child)
            
        for parent, child, direction in descriptions:
            distnodes.remove(child)
        rootval = distnodes.pop()

        treedict = defaultdict(lambda: [None, None])
        for parent, child, direction in descriptions:
            if direction == 1:
                treedict[parent][0] = child  
            else:
                treedict[parent][1] = child

        def buildtree(nodeval):
            if nodeval == None: return None
            p = TreeNode(nodeval)
            p.left = buildtree(treedict[nodeval][0])
            p.right = buildtree(treedict[nodeval][1])
            return p

        return buildtree(rootval)
