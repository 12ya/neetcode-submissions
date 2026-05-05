class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        for c in s1:
            window[c] = window.get(c, 0) + 1

        left = 0
        for right in range(len(s2)):
                
            char = s2[right]
            if right - left + 1 > len(s1):
                if s2[left] in window:
                    window[s2[left]] = window.get(s2[left], 0) + 1
                left += 1

            if char in window:
                window[char] -= 1

            if all(val == 0 for val in window.values()):
                return True
        
        return False
