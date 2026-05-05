class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charset, window = {}, {}

        for c in t:
            charset[c] = charset.get(c, 0) + 1

        have, need = 0, len(charset)
        result, resultLength = [-1, -1], float("inf")

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in charset:
                window[char] = window.get(char, 0) + 1
                if window[char] == charset[char]:
                    have += 1

            while have == need:
                if resultLength > right - left + 1:
                    resultLength = right - left + 1
                    result = [left, right]

                if s[left] in window:
                    window[s[left]] -= 1
                    if window[s[left]] < charset[s[left]]:
                        have -= 1

                left += 1

        l, r = result
        return s[l:r+1] if resultLength != float('inf') else ""