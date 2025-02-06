class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i]-min_price
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, profit)
        return max_profit