class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
        if not res:
            res.append([start, end])
        elif res[-1] != [start,end]:
            res.append([start, end])

        return res

        