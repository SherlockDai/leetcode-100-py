import heapq
class MeidanFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    def addNum(self, num):
        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap, -num)
            return
        if len(self.minHeap) == len(self.maxHeap):
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
        elif len(self.minHeap) - len(self.maxHeap) >= 1:
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) >= 1:
            if num > -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
                heapq.heappush(self.minHeap, -heapq.heapop(self.maxHeap))
    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]


sol = MeidanFinder()
sol.addNum(1)
sol.addNum(2)
print(sol.findMedian())
sol.addNum(3)
print(sol.findMedian())
sol.addNum(3)
print(sol.findMedian())
