class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        p_start, p_end = intervals[0]
        removed = 0
        for idx in range(1, len(intervals)):
            c_start, c_end = intervals[idx]
            if c_start < p_end:
                if c_end < p_end:
                    p_start, p_end = c_start, c_end
                removed += 1
            else:
                p_start, p_end = c_start, c_end
        return removed