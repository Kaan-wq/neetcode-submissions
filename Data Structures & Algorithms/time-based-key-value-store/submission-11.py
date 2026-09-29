class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key, [])
        lo, hi = 0, len(values) - 1
        best = ""
        while lo <= hi:
            mid = (hi + lo) // 2
            v, t = values[mid]
            if t == timestamp:
                return v
            elif t < timestamp:
                lo = mid + 1
                best = v
            else:
                hi = mid - 1
        return best