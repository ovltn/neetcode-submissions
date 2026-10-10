class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        local_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                local_min = min(prices[i], local_min)
            else:
                res = max(prices[i] - local_min, res)

        return res
