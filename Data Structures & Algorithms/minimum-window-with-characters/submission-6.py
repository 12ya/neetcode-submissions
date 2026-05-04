class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount, window = {}, {}


        for char in t:
            sCount[char] = sCount.get(char, 0) + 1

        need, have = len(sCount), 0
        res, resLen = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in sCount and window[char] == sCount[char]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in sCount and window[s[l]] < sCount[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float('infinity') else ""
        