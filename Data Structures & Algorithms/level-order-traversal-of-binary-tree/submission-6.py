# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([(root, 0)])
        lv = []
        while queue:
            node, level = queue.popleft()
            if len(lv) == level:
                lv.append([])
            lv[level].append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        return lv