# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes=deque([root])
        levels=0
        while nodes:
            levels+=1
            size=len(nodes)
            for i in range(size):
                node=nodes.popleft()
                if node.right:
                    nodes.append(node.right)
                if node.left:
                    nodes.append(node.left) 
        return levels               
                     

        