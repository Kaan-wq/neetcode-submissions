from heapq import heapify, heappop, heappushpop, heappush

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]