class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # frequency of chars in dict
        dict_s = {}
        # sliding window
        i = 0
        j = 0
        max_len = 0
        while j<len(s):
            dict_s[s[j]] = 1 + dict_s.get(s[j], 0)
            if (j-i+1)-max(dict_s.values())>k:
                dict_s[s[i]]-=1
                i+=1
            max_len = max(max_len, j-i+1)
            j+=1
        # Return length of longest sliding window
        return max_len