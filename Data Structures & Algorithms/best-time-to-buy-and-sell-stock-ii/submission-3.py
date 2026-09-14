"""
    Dynamic Programming (Bottom-up)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            dp[i][0] = max(dp[i+1][0], -prices[i] + dp[i+1][1]) # buy
            dp[i][1] = max(dp[i+1][1], prices[i] + dp[i+1][0]) # sell

        print(dp)
        return dp[0][0]
