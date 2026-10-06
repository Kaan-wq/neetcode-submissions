# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], m: int) -> int:
            if not node: return 0
            return (
                (1 if node.val >= m else 0)
                + dfs(node.left, max(node.val, m))
                + dfs(node.right, max(node.val, m))
            )
        return dfs(root, root.val)