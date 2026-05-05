class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        for right in range(k - 1, len(nums)):
            res.append(max(nums[left : right + 1]))

            left += 1

        return res