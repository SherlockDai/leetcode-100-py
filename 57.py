class Solution:
    def insert(self, intervals, newInterval):
        for index, interval in enumerate(intervals):
            if newInterval.end < interval.start:
                intervals.insert(index, newInterval)
                return intervals
            if newInterval.start > interval.end:
                continue
            if newInterval.start >= interval.start and newInterval.end <= interval.end:
                return intervals
            if newInterval.start >= interval.start:
                interval.end = newInterval.end
                return self.merge(index, intervals)
            if newInterval.end <= interval.end:
                interval.start = newInterval.start
                return self.merge(index, intervals)
        intervals.append(newInterval)
        return intervals
    def merge(self, start, intervals):
        for index in range(start + 1, len(intervals)):
            if intervals[index].start > intervals[start].end:
                break
            elif intervals[index].end > intervals[start].end:
                intervals[start].end = intervals[index].end
        return intervals[0:start + 1] + intervals[index:]


class Interval:
    def __init__(self, s= 0, e = 0):
        self.start = s
        self.end = e

sol = Solution()
interval1 = Interval(1,2)
interval2 = Interval(3, 5)
interval3 = Interval(6, 7)
interval4 = Interval(8, 10)
interval5 = Interval(12, 16)
newInterval = Interval(4, 8)
result = sol.insert([interval1, interval2, interval3, interval4, interval5], newInterval)
test = 1