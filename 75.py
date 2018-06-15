class Solution:
    def sortColors(self, nums):
        left, anchor, right = 0, 0, len(nums) - 1
        while anchor <= right:
            if nums[anchor] == 2:
                foo = nums[right]
                nums[right] = nums[anchor]
                nums[anchor] = foo
                right -= 1
            if nums[anchor] == 0:
                foo = nums[left]
                nums[left] = nums[anchor]
                nums[anchor] = foo
                left += 1
            anchor += 1
        return nums

sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))