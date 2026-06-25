class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # input: list of strings
        # output: strings grouped by anagrams 
        # duplicate strings also include
        # empty strings output as it is
        # all lower case
        # order of words in grps does not matter
        # brute: compare every string with every other string by sorting and checking O(n^2 * klogk)
        # optimal
        # loop through strs
        # add the sorted word in dict with value and append the word seen
        # check if the sorted word is in the dict, if yes then append as value to that sorted word
        # if not then add it into dictionary
        # O(n)
        hashmap = {}
        from collections import Counter
        for s in strs:
            key = "".join(sorted(s))
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return hashmap.values()

                
        

