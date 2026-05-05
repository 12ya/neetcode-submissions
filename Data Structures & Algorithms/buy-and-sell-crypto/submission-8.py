class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = float('-inf')

        left = 0
        for right in range(len(prices)):
            l_price, r_price = prices[left], prices[right]
            if r_price < l_price:
                left = right

            curr = max(curr, r_price - l_price)

        return curr