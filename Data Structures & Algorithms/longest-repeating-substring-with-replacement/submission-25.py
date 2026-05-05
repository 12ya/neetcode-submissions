class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        result = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            chars[char] = chars.get(char, 0) + 1

            if right - left + 1 > k + max(chars.values()):
                chars[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result