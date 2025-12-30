class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # input: prices array
        # output: max profit made when selling at high and buying at low

        # sliding window
        # initialize max profit
        # left ptr at 0
        # right ptr starting from 1
        # if value at right ptr>value at left ptr
            # calculate profit and save to maxprofit
        # return maxprofit
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r]>prices[l]:
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r
        return max_profit