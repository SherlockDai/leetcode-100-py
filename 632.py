import heapq

class Solution():
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        idx_start, idx_end, cur_max = 0, float('inf'), float('-inf')
        priority_heap = []
        for idx, list in enumerate(nums):
            priority_heap.append((list[0], idx, 0))
            cur_max = list[0] if cur_max < list[0] else cur_max
        heapq.heapify(priority_heap)
        while priority_heap:
            #fetch the current min
            cur_min = heapq.heappop(priority_heap)
            #update the result here, right before we exit the while loop
            if cur_max - cur_min[0] < idx_end - idx_start:
                idx_start, idx_end = cur_min[0], cur_max
            #check if we reach the end of the list
            if cur_min[2] == len(nums[cur_min[1]]) - 1:
                break
            #increase the corresponding list index by 1
            new_num = nums[cur_min[1]][cur_min[2] + 1]
            heapq.heappush(priority_heap, (new_num, cur_min[1], cur_min[2] + 1))
            cur_max = max(cur_max, new_num)
        return [idx_start, idx_end]

