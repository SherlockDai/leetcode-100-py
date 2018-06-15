class Solution:
    def myPow(self, x, n):
        memo = [None] * (n + 1)
        return self.myMemo(x, n, memo)
    def myMemo(self, x, n, memo):
        if n == 1:
            memo[n] = x
            return x
        if memo[n] is not None:
            return memo[n]
        smaller_case = n // 2
        result = self.myMemo(x, smaller_case, memo) * self.myMemo(x, n - smaller_case, memo);
        memo[n] = result
        return result

sol = Solution()
print(sol.myPow(5, 10))