from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2 + y**2, idx) for idx, (x, y) in enumerate(points)]
        heapify(distances)
        return [points[heappop(distances)[1]] for _ in range(k)]