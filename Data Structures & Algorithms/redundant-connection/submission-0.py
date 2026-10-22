class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n, redundant = len(edges)+1, None
        parent, size = list(range(n)), [1] * n

        def find(child: int) -> int:
            root = cur = child
            while parent[root] != root:
                root = parent[root]
            while parent[cur] != cur:
                parent[cur], cur = root, parent[cur]
            return root
        
        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                nonlocal redundant
                redundant = [a, b]
                return

            if size[root_a] < size[root_b]: root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        for a, b in edges:
            union(a, b)
        return redundant
        