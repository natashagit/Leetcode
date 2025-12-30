class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # input: string
        # output: length of longest substring without duplicates

        # sliding window keeping only the substring with non duplicate chars
        # keep max count of longest substring
        # create set to store chars
        # keep pointer at 0
        # loop through string
        # while char present in set remove first element of string in set
        # add new char to set
        # store into max_length the length of substring
            
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
