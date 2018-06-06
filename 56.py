class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        if intervals is None or len(intervals) <= 1:
            return intervals
        result = []
        intervals.sort(key = lambda  x: x.start)
        left, right = intervals[0].start, intervals[0].end
        for interval in intervals:
            if right >= interval.start:
                if right < interval.end:
                    right = interval.end
            else:
                result.append(Interval(left, right))
                left = interval.start
                right = interval.end
        else:
            result.append(Interval(left, right))
        return result

interval1 = Interval(1, 3)
interval2 = Interval(2, 6)
interval3 = Interval(8, 10)
interval4 = Interval(15, 18)

sol = Solution()
sol.merge(list([interval1, interval2, interval3, interval4]))

