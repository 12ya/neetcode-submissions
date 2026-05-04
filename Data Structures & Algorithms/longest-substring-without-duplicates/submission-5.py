class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            subset.add(s[r])
        return res
