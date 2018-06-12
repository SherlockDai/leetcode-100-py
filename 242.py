class Solution:
    def isAnagram(self, s, t):
        buckets_s = dict()
        buckets_t = dict()
        for c_s in s:
            buckets_s[c_s] = buckets_s.setdefault(c_s, 0) + 1
        for c_t in t:
            buckets_t[c_t] = buckets_t.setdefault(c_t, 0) + 1
        for key in buckets_s:
            if key not in buckets_t or buckets_t[key] != buckets_s[key]:
                return False
        for key in buckets_t:
            if key not in buckets_s:
                return False
        return True
sol = Solution()
s, t = "anagram", "nagarams"
print(sol.isAnagram(s, t))