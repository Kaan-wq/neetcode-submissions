# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None

        def dfs(node: Optional[TreeNode]) -> tuple(bool, bool):
            nonlocal lca
            if not node or lca is not None: return (False, False)

            left_dfs = dfs(node.left)
            right_dfs = dfs(node.right)

            found_p = node is p or left_dfs[0] or right_dfs[0]
            found_q = node is q or left_dfs[1] or right_dfs[1]

            if found_p and found_q and not lca:
                lca = node

            return (found_p, found_q)
        dfs(root)
        return lca