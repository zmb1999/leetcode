class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.d = collections.defaultdict(list)
        for index, value in enumerate(arr):
            self.d[value].append(index)
        self.freq = sorted([(len(locations), value) for value, locations in self.d.items()], reverse = True)

    def query(self, left: int, right: int, threshold: int) -> int:
        for f, v in self.freq:                                      #二分查找
            if f < threshold: break
            locations = self.d[v]
            low = bisect.bisect_left(locations, left)
            high = bisect.bisect_right(locations, right)
            if high - low >= threshold:
                return v
        return -1
