class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # Use a set for unique elements
        charSet = set()
        # Left iterator to remove element from start
        l = 0
        # Store max length of substring
        res = 0

        # Iterate through string s
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            # Add element to charSet
            charSet.add(s[r])
            # Store maximum length of substring in res
            res = max(res, r-l+1)
        return res