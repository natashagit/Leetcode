class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # input: prices array
        # output: max profit made when selling at high and buying at low
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right]-prices[left]>0:
                max_profit = max(max_profit, prices[right]-prices[left])
            else:
                left=right
        return max_profit

        
        


