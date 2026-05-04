class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_so_far = max(max_so_far, profit)
            else:
                l = r
            r += 1

        return max_so_far