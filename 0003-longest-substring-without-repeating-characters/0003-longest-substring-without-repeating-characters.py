class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # input: string
        # output: length of longest substring without duplicates

        # sliding window keeping only the substring with non duplicate chars
        # keep count of longest substring
        # store into a dictionary and if the count of any char>1
            # reduce count of first element from dict until count==1
        max_length = 0
        str_set = set()
        l=0
        for i in range(len(s)):
            while s[i] in str_set:
                str_set.remove(s[l])
                l+=1
            str_set.add(s[i])
            max_length = max(max_length, i-l+1)
        return max_length
