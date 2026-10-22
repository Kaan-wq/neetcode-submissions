class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent, size = list(range(n)), [1] * n
        groups = n

        def find(node: int) -> int:
            root = cur = node
            while parent[root] != root:
                root = parent[root]
            while parent[cur] != cur:
                parent[cur], cur = root, parent[cur]
            return root
        
        def union(a: int, b: int) -> None:
            p_a, p_b = find(a), find(b)
            if p_a == p_b: return

            if size[p_a] < size[p_b]: p_a, p_b = p_b, p_a
            parent[p_b] = p_a
            size[p_a] += size[p_b]
            
            nonlocal groups
            groups -= 1

        for a, b in edges: union(a, b)

        return groups
        