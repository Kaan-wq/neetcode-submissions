class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
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
        return sum(dfs(node) for node in range(n))