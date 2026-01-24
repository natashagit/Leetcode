class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 1 0 1
        # 1 0 0
        # input: a and b
        # output: sum of a and b
        # while carry is done
        # take XOR -> to get sum
        # take carry by a&b -> shift to right 
        # add carry to sum
       
        MASK = 0xFFFFFFFF        # keep lowest 32 bits
        MAX_INT = 0x7FFFFFFF     # largest 32-bit signed int
        while b!=0:
            carry = a&b & MASK
            carry<<=1
            a = (a^b) & MASK
            b = carry & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)
