class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        p_end = intervals[0][1]
        removed = 0
        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            if start < p_end:
                if end < p_end:
                    p_end = end
                removed += 1
            else:
                p_end = end
        return removed