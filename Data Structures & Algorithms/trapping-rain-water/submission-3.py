class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = water = maxR = 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if height[l] < height[r]:
                l += 1
                trapped = maxL - height[l]
                if trapped > 0:
                    water += trapped
            else:
                r -= 1
                trapped = maxR - height[r]
                if trapped > 0:
                    water += trapped

        return water