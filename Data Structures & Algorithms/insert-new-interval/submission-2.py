class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        result = []
        n_start, n_end = newInterval
        for idx, (start, end) in enumerate(intervals):
            if end < n_start:
                result.append([start, end])
            elif n_end < start:
                result.append([n_start, n_end])
                return result + intervals[idx:]
            else:
                n_start = min(n_start, start)
                n_end = max(n_end, end)
        result.append([n_start, n_end])
        return result