class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        maxL = maxR = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL > maxR:
                r -= 1
                trapped = maxR - height[r]
                if trapped > 0:
                    water += trapped
            else:
                l += 1
                trapped = maxL - height[l]
                if trapped > 0:
                    water += trapped

        return water

            
            
