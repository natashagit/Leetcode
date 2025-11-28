class Solution(object):
    # input: two strings s and t
    # output: return true if t is an anagram of s
    # counter from collections
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            if s[i] in count_s:
                count_s[s[i]]+=1
            else:
                count_s[s[i]]=1
        
        for i in range(len(t)):
            if t[i] in count_t:
                count_t[t[i]]+=1
            else:
                count_t[t[i]]=1
        
        for key in count_s:
            if count_s[key]!=count_t.get(key,0):
                return False
        return True
        