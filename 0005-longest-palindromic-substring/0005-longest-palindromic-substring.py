class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time Complexity O(n^3)
        def ispalindrome(s, left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        n = len(s)
        for right in range(n, 0, -1):
            for left in range(n-right+1):
                if ispalindrome(s, left, left+right-1):
                    return s[left:left+right] 
        return ""


        
