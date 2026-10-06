# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        state: dict[int, list[TreeNode]] = {}

        def height(node: Optional[TreeNode], h: int) -> None:
            if not node: return
            h_new = h + 1
            state.setdefault(h_new, []).append(node.val)
            height(node.left, h_new)
            height(node.right, h_new)
        
        height(root, -1)
        return list(state.values())
