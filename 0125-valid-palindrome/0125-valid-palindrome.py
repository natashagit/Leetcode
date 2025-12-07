class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # input: string, which needs to be cleaned up
        # output: true/false 
        # edge case: one letter, empty-> true

        # preprocess string by removing non alphanumeric chars
        # left point and right pointer at start and end of string
        # loop through till left!=right pointer
        # keep checking if the value is not equal-> return False
        # In the end return True

        s = "".join([i for i in s if i.isalnum()])
        s = s.lower()
        if len(s)<=1:
            return True
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True