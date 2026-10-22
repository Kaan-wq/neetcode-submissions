class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components, visited = 0, set()
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int):
            if node in visited: return False

            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)
            return True
        
        for node in range(n):
            components += dfs(node)
        return components