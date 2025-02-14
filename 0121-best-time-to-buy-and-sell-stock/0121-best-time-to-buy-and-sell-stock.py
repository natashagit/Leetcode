class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time Complexity = O(n)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i]-min_price
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, profit)
        return max_profit

        # Time Complexity = O(n^2)
        # n = len(prices)
        # max_profit = 0
        # for i in range(n):  # Buying day
        #     for j in range(i + 1, n):  # Selling day (must be after buying day)
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit