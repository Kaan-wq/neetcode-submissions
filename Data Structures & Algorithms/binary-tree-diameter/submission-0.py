# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def height(r: Optional[TreeNode]) -> int:
            nonlocal best
            if not r: return 0
            l, r = height(r.left), height(r.right)
            best = max(best, l + r)
            return 1 + max(l, r)
            
        height(root)
        return best