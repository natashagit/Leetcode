class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        n = x
        last = 0
        if x<0:
            return False
        if x==0:
            return True
        while n!=0:
            last = last*10 + (n%10)
            n = n//10
        
        if last == x:
            return True
        return False
            

