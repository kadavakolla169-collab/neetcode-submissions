class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        left = 0
        right = len(self.data[key]) - 1
        result = ""
        while left<=right:
            mid = (left + right) // 2
            if self.data[key][mid][1] <= timestamp:
                result = self.data[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result
             

