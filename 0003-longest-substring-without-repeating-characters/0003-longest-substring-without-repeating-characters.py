class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # input: string with duplicate chars
        # output: length of longest substring without duplicate chars
        # empty string -> 0
        # one char -> 1
        # numbers or special chars - yes
        # size of string
        # output only the length, not the string
        # abcbacbb
        # brute force
        # loop through string   
        # have a dictionary for each starting char  {a:1, b:1, c:1}
        # store length of string by taking number of keys in dictionary
        # O(n^2)
        # Optimal 
        # sliding window approach
        # we keep an index at start and second that moves through as sliding and
        # add to set each char
        # we store length of set in maxlength
        # when we see char already present in set, we remove leftmost char until char not already present from set
        string_set = set()
        length = 0
        i = j = 0
        while j<len(s):
            while s[j] in string_set:
                string_set.remove(s[i])
                i+=1
            string_set.add(s[j])
            length = max(length, len(string_set))
            j+=1
        return length