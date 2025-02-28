class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Setting to 32bit number
        mask = 0xffffffff
        while (mask&b)>0:
            temp = (a&b)<<1
            a = a^b
            b = temp
        return (mask&a) if b>0 else a
        # Overflow as carry more than 32 bit
        # while b!=0:
        #     # Saving for carry on with left shift
        #     temp = (a&b)<<1
        #     # XOR operation for addition
        #     a = a^b
        #     # Setting b as temp to do XOR with again
        #     b = temp
        # return a