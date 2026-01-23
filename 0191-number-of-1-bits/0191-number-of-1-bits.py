class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # input: integer n
        # output: number of 1's in the binary rep
        # use n&1 to see if last digit is 1
        # keep removing last digit by shifting right n>>=1
        # keep a count of 1's
        count = 0
        while n:
            if n&1==1:
                count+=1
            n>>=1
        return count