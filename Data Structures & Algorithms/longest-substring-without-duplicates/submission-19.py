class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        result = 1

        left = 0
        charset = set(s[0])
        for right in range(1, len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left +=1

            charset.add(s[right])
            result = max(result, right - left + 1)

        return result
