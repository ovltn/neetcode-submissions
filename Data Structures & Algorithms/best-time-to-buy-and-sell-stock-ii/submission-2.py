"""
    Dynamic Programming (Top-down)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def rec(i, bought):
            if (i, bought) in dp:
                return dp[(i, bought)]

            if i == len(prices): # base
                return 0

            res = rec(i+1, bought) # skip
            if bought:
                res = max(res, prices[i] + rec(i+1, False)) # sell
            else:
                res = max(res, -prices[i] + rec(i+1, True)) # buy
            dp[(i, bought)] = res
            return res

        return rec(0, False)
