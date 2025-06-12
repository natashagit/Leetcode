class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window with l and r
        l=0
        # Keep a count
        count = {}
        # Keep max length
        max_length = 0
        # loop through string with r to extend window
        for r in range(len(s)):
            count[s[r]]= 1+ count.get(s[r], 0)
            print(count)
            if (r-l+1)-(max(count.values()))<=k:
                max_length = max(max_length, r-l+1)
            else:
                count[s[l]]-=1
                l+=1
        return max_length