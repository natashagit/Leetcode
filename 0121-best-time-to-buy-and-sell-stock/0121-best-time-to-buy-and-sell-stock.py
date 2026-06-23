class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # input: prices of stock on each day
        # output: maximum profit
        # if only one element
        # if only 2 elements
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(prices[i]-min_price,max_profit)
            min_price = min(prices[i], min_price)
        return max_profit
