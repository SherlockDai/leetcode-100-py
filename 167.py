class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while numbers:
            cur_sum = numbers[left] + [right]
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            elif cur_sum == target:
                break
        return [left, right]