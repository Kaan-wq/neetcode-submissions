# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not node: return True
            return (
                lower < node.val < upper
                and dfs(node.left, lower, node.val)
                and dfs(node.right, node.val, upper)
            )
        return dfs(root, float("-inf"), float("inf"))