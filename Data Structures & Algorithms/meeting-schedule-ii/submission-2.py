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
        rooms = 0
        if not intervals: return rooms

        intervals.sort(key=lambda x: x.start)
        heap = []

        for el in intervals:
            while heap and heap[0] <= el.start: heappop(heap)
            heappush(heap, el.end)
            rooms = max(rooms, len(heap))
        return rooms
