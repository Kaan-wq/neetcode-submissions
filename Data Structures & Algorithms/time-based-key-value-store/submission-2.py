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
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
            best = values[mid] if values[mid][1] >= best[1] and values[mid][1] <= timestamp else best
        return best[0] if best[1] <= timestamp else ""
