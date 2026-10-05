# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if bool(p) != bool(q): return False
        if not p: return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if root and not subRoot: return False
        if not root and subRoot: return False

        return (
            (
                root.val == subRoot.val
                and self.isSameTree(root, subRoot)
            )
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )