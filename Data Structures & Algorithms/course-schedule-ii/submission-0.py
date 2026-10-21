class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        col = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        
        def dfs(node: int) -> bool:
            if col[node] == 2: return True
            if col[node] == 1: return False

            col[node] = 1
            for child in adj[node]:
                if not dfs(child): return False
            col[node] = 2
            order.append(node)
            return True

        if all(dfs(node) for node in range(numCourses)):
            return order[::-1]
        return []