class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0 
        charset = set()

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            res = max(res, right - left + 1)
        return res