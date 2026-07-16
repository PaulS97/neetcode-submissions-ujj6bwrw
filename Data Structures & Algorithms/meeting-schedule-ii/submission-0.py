"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        starts.sort()
        ends = [interval.end for interval in intervals]
        ends.sort()

        i=0
        j=0
        used = 0
        maxused = 0
        while(i<len(starts)):
            if starts[i]<ends[j]:
                used += 1
                maxused = max(used, maxused)
                i+= 1
            else:
                used -= 1
                j += 1

        return maxused






        