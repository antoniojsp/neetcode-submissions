# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(node, level):
            if not node:
                return 0
            return max(bfs(node.left, level+1), bfs(node.right, level+1)) + 1


        return bfs(root, 0)
