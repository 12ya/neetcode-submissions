class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''
        window, countT = {}, {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have, need = 0, len(countT)

        l = 0 

        res, resLen = [-1, -1], float('infinity')
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1


        l, r = res

        return s[l:r + 1] if resLen != float('infinity') else ''

        
