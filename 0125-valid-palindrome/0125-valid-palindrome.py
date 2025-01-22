class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ''.join([st for st in s if st.isalnum()]).lower()
        start = 0
        end = len(st)-1
        while(start<end):
            if st[start]!=st[end]:
                return False
            else:
                start+=1
                end-=1
        return True