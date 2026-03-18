class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # input: prices of stocks
        # output: max profit after buying and selling on multiple days
        # constraints: n -> 10^4
        # edge cases: only one stock, empty array -> 0, negative->0
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if buy<price:
                profit+=price-buy
            buy = price
        return profit

        