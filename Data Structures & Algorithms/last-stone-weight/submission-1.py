from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        heapify(heap)

        while len(heap) > 1:
            y = -heappop(heap)
            x = -heappop(heap)

            if x < y:
                heappush(heap, x - y)
        return -heap[0] if heap else 0