class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Keep a count dictionary for frequency of characters
        count = {}
        # Result to store longest window size
        result = 0
        # Left pointer for start of window
        l=0
        # Looping through elements in window
        for r in range(len(s)):
            # Update dictionary with cunt of elements
            count[s[r]] = 1 +count.get(s[r], 0)
            # check if window size - max frequency of element exceeding k (number of replacements)
            while (r-l+1) - max(count.values())> k:
                # Decrement first element frequency in count by 1
                count[s[l]]-=1
                # If it exceeds, shift l ahead
                l+=1
            # Result contains maximum window size
            result = max(result, r-l+1)
        return result