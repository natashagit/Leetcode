class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # input: string ABAB
        # output: length of the longest substring that has duplicate chars after changing chars K times max
        # empty string -> 0
        # one char string -> 1
        # only uppercase enlish letters
        # k=0 -> already longest repeating one
        # max k -> can be lesser
        # brute force
        # check every substring
        # replace the least frequent char
        # keep count of chars in dict
        # window length - most frequent count <=k for it to be valid
        # O(n^2 * 26) and space O(26)
        # Optimal approach
        # sliding window
        # keep a dict
        # if (window length - most frequent count) > k 
        # reduce count of leftmost element from dict
        # keep maxlength as windowlength
        dict_map = {}
        i = 0
        maxLength = 0 #AABABBA
        windowLength = 0
        for j in range(len(s)): #j=4 i=1
            if s[j] not in dict_map: #s[j] = B
                dict_map[s[j]] = 1 #dict_map = {A:2, B:2}
            else:
                dict_map[s[j]] += 1
            windowLength = j-i+1 #windowLength = 5
            while windowLength - max(dict_map.values())>k: #5-3 = 2 >1
                dict_map[s[i]]-=1 
                i+=1
                windowLength-=1
            maxLength = max(windowLength, maxLength) #maxLength = 4
        return maxLength

