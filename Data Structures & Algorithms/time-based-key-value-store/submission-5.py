class TimeMap:

    def __init__(self):
        self.time_map: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key, [])
        lo, hi = 0, len(values) - 1
        best = ["", float("-inf")]
        while lo <= hi:
            mid = (hi + lo) // 2
            val, t = values[mid]
            if t == timestamp:
                return val
            elif t < timestamp:
                lo = mid + 1
                best = values[mid]
            else:
                hi = mid - 1
        return best[0]
