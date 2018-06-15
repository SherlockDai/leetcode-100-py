class Solution:
    def grayCode(self, n):
        result = []
        result.append(0)
        for i in range(0, n):
            size = len(result)
            while size > 0:
                result.append((1 << i) + result[size - 1])
                size -= 1
        return result

sol = Solution()
print(sol.grayCode(3))