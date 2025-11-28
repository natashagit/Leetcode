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
        from collections import Counter
        t_counter = Counter(t)
        s_counter = Counter(s)
        if t_counter==s_counter:
            return True
        return False
        