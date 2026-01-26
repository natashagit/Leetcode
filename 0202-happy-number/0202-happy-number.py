class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # input: number with 2 digits
        # output: true/false if its a happy number
        
        def next_number(n):
            total = 0
            while n>0:
                digit = n%10
                total+=digit*digit
                n //=10
            return total

        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = next_number(n)
        return True
