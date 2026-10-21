class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return True

        return all(dfs(node) for node in range(numCourses))