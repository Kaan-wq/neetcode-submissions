# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def height(r: Optional[TreeNode]) -> int:
            nonlocal is_balanced
            if not r: return 0
            left, right = height(r.left), height(r.right)
            print(f"Root {r.val} L {left} R {right}")
            if abs(left - right) > 1: is_balanced = False
            return 1 + max(left, right)

        height(root)
        return is_balanced