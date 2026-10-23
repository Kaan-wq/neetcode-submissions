class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph, visited = [[] for _ in range(n)], set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for child in graph[node]:
                if child == parent: continue
                if (child in visited) or (not dfs(child, node)): return False
            return True
        
        return dfs(0, None) and len(visited) == n