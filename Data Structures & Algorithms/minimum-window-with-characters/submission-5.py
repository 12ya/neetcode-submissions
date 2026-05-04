class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        window, count = {}, {}

        for char in t:
            count[char] = count.get(char, 0) + 1
        
        res, resLen = [-1, -1], float('infinity')
        have, need = 0, len(count)
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in count and window[char] == count[char]:
                have += 1
            
            while have == need:
                window[s[l]] -= 1
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float('infinity') else ""
                
