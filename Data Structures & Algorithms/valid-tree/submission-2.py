class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        visited = set()
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, parent: int) -> bool:
            # print(f"Node {node} in visited ? {node in visited}")
            if node in visited: return False

            visited.add(node)
            # print(f"Visited Nodes {visited}")
            # print("Recursing...")
            for neighbour in graph[node]:
                if neighbour == parent:
                    # print(f"Skipping parent {parent}")
                    continue
                # print(f"Recursing with parent {node} and neighbour {neighbour}")
                if not dfs(neighbour, node): return False
            return True

        dfs(0, None)
        return True if len(visited) == n else False