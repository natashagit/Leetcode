class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            # shift result right 
            result <<=1
            # add the rightmost bit
            result = result | (n&1)
            # shift left
            n>>=1
        return result