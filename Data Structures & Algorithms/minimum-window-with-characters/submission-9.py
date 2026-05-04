class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count, window = {}, {}

        for c in t:
            count[c] = count.get(c, 0) + 1

        have, need = 0, len(count)
        res, resLen = [-1, -1], float("inf")

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in count:
                window[char] = window.get(char, 0) + 1

            if char in count and window[char] == count[char]:
                have += 1

            while have == need:
                if resLen > right - left + 1:
                    res = [left, right]
                    resLen = right - left + 1

                if s[left] in window:
                    window[s[left]] -= 1
                    
                if s[left] in window and window[s[left]] < count[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l : r + 1] if resLen != float("inf") else ""
