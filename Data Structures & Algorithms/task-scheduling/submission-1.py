from collections import deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_num = {}
        for task in tasks:
            tasks_num[task] = tasks_num.get(task, 0) - 1
        heap = list(tasks_num.values())
        heapify(heap)

        time = 0
        queue = deque()
        while heap or queue:
            if heap:
                task = heappop(heap) + 1
                if task < 0:
                    queue.append((task, time + n))
            if queue and queue[0][1] == time:
                heappush(heap, queue.popleft()[0])
            
            time += 1
        return time