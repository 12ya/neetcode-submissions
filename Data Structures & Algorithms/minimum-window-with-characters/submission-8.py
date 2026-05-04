class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        char_set, window = {}, {}
        for c in t:
            char_set[c] = char_set.get(c, 0) + 1

        left = 0

        have, need = 0, len(char_set)

        res, resLen = [-1, -1], float("inf")

        for right in range(len(s)):
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1

            if curr in char_set and window[curr] == char_set[curr]:
                have += 1

            while have == need:
                if resLen > right - left + 1:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in char_set and window[s[left]] < char_set[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
