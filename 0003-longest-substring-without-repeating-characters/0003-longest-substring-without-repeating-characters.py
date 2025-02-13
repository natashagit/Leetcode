class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window to keep check of all substrings
        maxi=0
        if len(s)==1:
            return 1
        for i in range(len(s)):
            sub={}
            for j in range(i, len(s)):
                if s[j] not in sub:
                    sub[s[j]]=1
                else:
                    if maxi<len(sub):
                        maxi=len(sub)
                    break
                if maxi<len(sub):
                    maxi=len(sub)
        return maxi


