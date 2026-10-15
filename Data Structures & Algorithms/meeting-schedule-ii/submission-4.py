"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        intervals.sort(key=lambda x: x.start)
        heap, rooms = [], 0

        for el in intervals:
            if heap and heap[0] <= el.start: heappop(heap)
            heappush(heap, el.end)
            rooms = max(rooms, len(heap))
        return rooms
