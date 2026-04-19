class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # input: string s and length k
        # output: max count of vowels in window k
        # constraint on s -> 10^5
        # edge cases: string empty
        set_v = {'a', 'e', 'i', 'o', 'u'}
        curr = 0
        for i in range(k):
            if s[i] in set_v:
                curr+=1
        max_v = curr
        for i in range(k, len(s)):
            if s[i] in set_v:
                curr+=1
            if s[i-k] in set_v:
                curr-=1
            max_v = max(curr, max_v)
        return max_v
            
