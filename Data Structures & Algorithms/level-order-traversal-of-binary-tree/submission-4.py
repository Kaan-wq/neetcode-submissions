# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        state: dict[int, list[int]] = {}

        def depth(node: Optional[TreeNode], h: int) -> None:
            if not node: return
            state.setdefault(h, []).append(node.val)
            depth(node.left, h + 1)
            depth(node.right, h + 1)
        
        depth(root, 0)
        return list(state.values())
