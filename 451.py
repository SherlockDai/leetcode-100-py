class Solution:
    def frequencySort(self, s):
        map = dict()
        result = ""
        for c in s:
            map[c] = map.setdefault(c, 0) + 1
        #instead of using the built-in sort function which is probably using quick sort, let us use bucket sort
        buckets = [None] * (len(s) + 1)
        for key in map:
            if buckets[map[key]] is None:
                buckets[map[key]] = [key]
            else:
                buckets[map[key]].append(key)
        for index, bucket in reversed(list(enumerate(buckets))):
            if bucket is None:
                continue
            for key in bucket:
                result += key * index
        return result

sol = Solution()
params = "Aabb";
print(sol.frequencySort(params))