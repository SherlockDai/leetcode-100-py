import random
class Solution:
    def findKthLargest(self, nums, k):
        end = len(nums) - 1
        start = 0
        return self.quickFind(nums, start, end, k - 1)
    def quickFind(self, nums, start, end, k):
        #get the random pivot
        pivot_index = random.randint(start, end)
        pivot = nums[pivot_index]
        #move the
        foo = nums[end]
        nums[end] = nums[pivot_index]
        nums[pivot_index] = foo
        #intialize slow and fast
        slow = fast = start
        for fast in range(start, end):
            if nums[fast] > pivot:
                fast += 1
            else:
                #swap slow and fast
                foo = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = foo
                slow += 1
                fast += 1
        #swap pivot and slow
        nums[end] = nums[slow]
        nums[slow] = pivot
        pivot_index = slow
        if pivot_index == k:
            return pivot
        elif pivot_index > k:
            return self.quickFind(nums, start, pivot_index - 1, k)
        else:
            return self.quickFind(nums, pivot_index + 1, end, k)











sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))