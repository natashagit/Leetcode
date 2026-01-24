class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # input: integer n
        # output: reversed bits integer of n
        # loop through 32
        # take last bit of n and add it to result from the left
        # shift result to right and add last bit of n to it
        # keep shifting n to left
        result = 0
        for _ in range(32):
            # shift result right 
            result <<=1
            # add the rightmost bit
            result = result | (n&1)
            # shift left
            n>>=1
        return result