class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        char_set = {}
        window = len(s1) - 1

        for c in s1:
            char_set[c] = char_set.get(c, 0) + 1
        

        for right in range(len(s2)):
            if right - left > window:
                if s2[left] in char_set:
                    char_set[s2[left]]+=1
                left += 1
            
            if s2[right] in char_set:
                char_set[s2[right]] -= 1
            
            if all(val == 0 for val in char_set.values()):
                return True

        return False