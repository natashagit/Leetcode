class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # empty string and single char- true
        # numbers?
        # Brute force
        # clean the string
        # compare string with its reverse
        # O(n) time and O(n) space
        # Optimal approach
        # two pointers from start and end
        # keep checking if not alphanumberic and skip the spaces
        # check lower case left and right strings
        # O(n) time and O(1) space
        left = 0
        right = len(s)-1

        while left<right:
            while left<right and not s[left].isalnum():
                left+=1

            while left<right and not s[right].isalnum():
                right-=1
            
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
        
            
