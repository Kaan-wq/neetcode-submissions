"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(start: Optional['Node']) -> Optional['Node']:
            if not start: return
            if start.val in visited: return visited[start.val]
            
            clone = Node(start.val)
            visited[start.val] = clone
            clone.neighbors = [dfs(adj) for adj in start.neighbors]

            return clone
        return dfs(node)