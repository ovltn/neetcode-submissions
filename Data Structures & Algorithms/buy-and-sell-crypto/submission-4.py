class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        current_min = prices[0]

        for i in range(1, len(prices)):
            current_min  = min(prices[i], current_min)
            benefit = max(prices[i] - current_min, benefit)

        return benefit