class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        so_far = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                so_far = max(so_far, profit)
            else:
                l = r
            r += 1

        return so_far