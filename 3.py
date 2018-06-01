class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left = 0, 0
        map = dict()
        for idx, c in enumerate(s):
            if c in map:
                if left <= map[c]:
                    left = map[c] + 1
                result = max(result, idx - left + 1)

            else:
                result = max(result, idx - left + 1)
            map[c] = idx
        return result