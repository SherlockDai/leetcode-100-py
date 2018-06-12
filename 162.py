class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        return self.findPeak(nums, start, end)

    def findPeak(self, nums, start, end):
        mid = (start + end) // 2
        # we only move upwards, if we are at the begining or end of the array we find the peak
        if mid == 0 or mid == len(nums) - 1:
            return mid
        if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            # intuitive that we find the peak
            return mid
        if nums[mid - 1] < nums[mid]:
            # find peak in right side of the mid
            return self.findPeak(nums, mid + 1, end)
        elif nums[mid + 1] < nums[mid]:
            return self.findPeak(nums, start, mid - 1)
        else:
            # this situation means the mid is now in the valley, we go left
            return self.findPeak(nums, start, mid - 1)


sol = Solution()
print(sol.findPeakElement([1,2,3,1]))