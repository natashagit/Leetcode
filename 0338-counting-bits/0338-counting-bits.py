class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # input: integer n
        # output: array consisting of number of 1's for all integers upto n

        def count_1(n):
            count = 0
            while n:
                if n&1:
                    count+=1
                n>>=1
            return count
        result = []
        for i in range(n+1):
            result.append(count_1(i))
        
        return result