class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyStore:
            self.keyStore[key].append((value, timestamp))
        else:
            self.keyStore[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        res, vals = '', self.keyStore.get(key, [])
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
