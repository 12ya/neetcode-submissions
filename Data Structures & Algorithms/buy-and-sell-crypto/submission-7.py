class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        result = float("-inf")

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            
            curr = prices[right] - prices[left]

            result = max(result, curr)

        return result if result != float("-inf") else 0
        