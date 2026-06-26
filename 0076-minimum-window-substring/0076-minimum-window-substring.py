class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # input: s="ADOBECODEBANC" and t="ABCB"
        # output: shortest substring with chars of t in s: "BANC"
        # t not in s-> ""
        # empty s -> ""
        # t-> 1 char; "A" if in s
        # all chars uppercase english letters?
        # brute force
        # Loop through s and check if every substring contains all chars of t
        # O(n^2)
        # Optimal
        # sliding window
        # loop through s with two pointers
        # right pointer moves and keeps adding char to window
        # track if values meeting validity of chars in t ->store length
        # once meets all of t 
        # shrink window from left
        # update minlength
        if not s or not t:
            return ""
        from collections import Counter, defaultdict
        dict_t = Counter(t)
        window = defaultdict(int)
        left= 0
        formed = 0
        required = len(dict_t)
        min_len = float("inf")
        result = ""
        for right in range(len(s)):
            window[s[right]]+=1
            if s[right] in dict_t and dict_t[s[right]]==window[s[right]]:
                formed+=1
            
            while formed==required:
                if right-left+1<min_len:
                    min_len = right-left+1
                    result = s[left:right+1]
                
                window[s[left]]-=1
                if s[left] in dict_t and window[s[left]]<dict_t[s[left]]:
                    formed-=1
                left+=1
        return result
            


            

            

            
            
        
        
