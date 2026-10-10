class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        local_min = prices[0]
        
        for i in range(1, len(prices)):
            local_min = min(prices[i], local_min)
            res = max(prices[i] - local_min, res)

        return res
