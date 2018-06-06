class Solution:
    def functionName(self, nums, k):
        map = dict()
        result = []
        for num in nums:
            map[num] = map.setdefault(num, 0) + 1
        buckets = [None] * (len(nums) + 1)
        for key in map:
            if buckets[map[key]] is None:
                buckets[map[key]] = [key]
            else:
                buckets[map[key]].append(key)
        for bucket in reversed(buckets):
            if k == 0:
                break;
            if bucket is None:
                continue
            for key in bucket:
                if k == 0:
                    break;
                result.append(key)
                k -= 1
        return result

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.functionName(nums, k))