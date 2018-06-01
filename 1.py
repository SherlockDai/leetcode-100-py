class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, num in enumerate(nums):
            if (target - num) in map:
                return [map[target - num], idx].sort()
            map[num] = idx
