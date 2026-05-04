class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        
        need = len(count1)
        for i in range(len(s2)):
            count2, curr = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    curr += 1
                if curr == need:
                    return True
        return False
