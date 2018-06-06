class Solution:
    def threeSum(self, nums):
        if nums is None or len(nums) < 3:
            return []
        result = list()
        nums.sort()
        pointer = 0
        prevNum = float('-inf')
        for pointer in range(len(nums) - 2):
            left, right = pointer + 1, len(nums) - 1
            if prevNum == nums[pointer]:
                #we used this number as the head already
                continue
            while left < right:
                target = 0 - nums[pointer]
                if nums[left] + nums[right] == target:
                    # we find one!
                    result.append([nums[pointer], nums[left], nums[right]])
                    left += 1
                elif nums[left] + nums[right] < target:
                    #left side needs to grow in order to get larger sum
                    left += 1
                else:
                    #right side needs to shrink in order to get smaller sum
                    right -= 1
            prevNum = nums[pointer]
        return result

sol = Solution()
params = [-1, 0, 1, 2, -1, 4] ;
print(sol.threeSum(params))