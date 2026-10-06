# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        smallest = None
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal count
            nonlocal smallest
            if not node: return
            if not smallest:
                dfs(node.left)
            count += 1
            if count == k:
                smallest = node
            if not smallest:
                dfs(node.right)
        dfs(root)
        return smallest.val