# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, smallest = 0, None
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal count, smallest
            if not node or smallest is not None: return
            dfs(node.left)
            count += 1
            if count == k:
                smallest = node.val
                return
            dfs(node.right)
        dfs(root)
        return smallest