class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = {}
        for char in s1:
            s1count[char] = s1count.get(char, 0) + 1

        needed = len(s1count)
        
        for i in range(len(s2)):
            s2count, curr = {}, 0
            for j in range(i, len(s2)):
                s2count[s2[j]] = s2count.get(s2[j], 0) + 1
                if s2count.get(s2[j], 0) > s1count.get(s2[j], 0):
                    break
                
                if s2count.get(s2[j], 0) == s1count.get(s2[j], 0):
                    curr += 1
                
                if curr == needed:
                    return True
        
        return False
                
