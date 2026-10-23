class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        visited = set()
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent: continue
                if neighbour in visited: return False
                if not dfs(neighbour, node): return False
            return True
        
        return dfs(0, None) and len(visited) == n