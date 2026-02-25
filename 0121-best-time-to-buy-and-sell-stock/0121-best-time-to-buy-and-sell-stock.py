class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # input: array of prices on each day i
        # output: maximum profit
        min_price = float("inf")
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, (p-min_price))
            min_price = min(p, min_price)

        return max_profit

        
        


