# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, max_p = prices[0], 0

        for i in range(1, len(prices)):
            buy = min(buy,prices[i])
            max_p = max(max_p, prices[i] - buy)
        
        return max_p