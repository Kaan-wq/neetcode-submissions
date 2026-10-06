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
            m_new = max(node.val, m)
            return (
                (node.val >= m)
                + dfs(node.left, m_new)
                + dfs(node.right, m_new)
            )
        return dfs(root, root.val)