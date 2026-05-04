class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        builder = ""

        for char in s:
            if char.isalnum():
                builder += char

        left, right = 0, len(builder) - 1

        while left < right:
            if builder[left] != builder[right]:
                return False
            left += 1
            right -= 1

        return True