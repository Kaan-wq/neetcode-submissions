class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        new_start, new_end = newInterval[0], newInterval[1]
        inserted = False
        for idx, (start, end) in enumerate(intervals):
            if new_start < start:
                intervals.insert(idx, newInterval)
                inserted = True
                break
        if not inserted: intervals.append(newInterval)

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            p_start, p_end = result.pop()
            c_start, c_end = intervals[i]
            if c_start <= p_end:
                result.append([p_start, max(p_end, c_end)])
            else:
                result.append([p_start, p_end])
                result.append([c_start, c_end])
        return result