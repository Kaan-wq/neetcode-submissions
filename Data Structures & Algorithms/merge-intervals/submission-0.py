class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            p_start, p_end = result.pop()
            c_start, c_end = intervals[i]
            if p_start <= c_end and c_start <= p_end:
                result.append([p_start, max(p_end, c_end)])
            else:
                result.append([p_start, p_end])
                result.append([c_start, c_end])
        return result