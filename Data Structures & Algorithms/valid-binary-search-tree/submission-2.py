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
            #print(f"{lower} < {node.val} < {upper}")

            return (
                lower < node.val < upper
                and dfs(node.left, lower, min(upper, node.val))
                and dfs(node.right, max(node.val, lower), upper)
            )
        return dfs(root, float("-inf"), float("inf"))