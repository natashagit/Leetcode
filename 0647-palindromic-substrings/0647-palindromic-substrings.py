class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time Complexity = O(n^2)
        res=0
        
        for i in range(len(s)):
            # For odd number string palindromes
            l = r = i
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    res+=1
                    r+=1
                    l-=1
                else:
                    break
            # For even number string palindromes
            l = i
            r = i+1
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    res+=1
                    r+=1
                    l-=1
                else:
                    break
        return res