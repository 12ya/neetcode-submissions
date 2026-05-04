class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        hm = set()
        res = 0

        for R in range(len(s)):
            while s[R] in hm:
                hm.remove(s[L])
                L += 1
            hm.add(s[R])
            res = max(res, R - L + 1)
        
        return res