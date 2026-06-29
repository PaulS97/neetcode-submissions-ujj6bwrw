class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""



        stamps = self.store[key]

        if stamps[0][0] > timestamp:
            return ""
        else:
            best = 0

        l, r = 0, len(stamps) - 1

        count = 0
        while(l<=r):
            count += 1
            mid = (l+r) // 2
            midval = stamps[mid][0]
 

            if midval > timestamp:
                r = mid - 1
            elif midval < timestamp:
                best = max(best, mid)
                l = mid + 1
            else:
                best = mid
                break
        return stamps[best][1]

        
