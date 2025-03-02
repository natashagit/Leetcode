class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            # Take right shift till 32 to get all bits by taking & with 1
            bit = (n>>i)&1
            # Take 31st bit onwards left shift to start from end and add to original bits with OR
            res = res | (bit<<(31-i))
        return res